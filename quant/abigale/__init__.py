"""
quant.abigale is a python module that supports Abigale Project.
It was originally part of the Abigale Project called AbiClient.
It helps upload timeseries data and backtest results to servers.
"""
import getpass
from ..common.settings import CONFIG
from .api import RestAPI
from .serializers import DataFrameSerializer
from .security import sha256
from . import api, exceptions, versioncontrol


__all__ = ['RestAPI', 'exceptions', 'sha256', 'versioncontrol', 'api']


class Abigale:
    """
    Abigale Client
    """
    def __init__(self, host=None, port=None, root=None):
        host = host or CONFIG.ABIGALE_HOST
        port = port or CONFIG.ABIGALE_PORT
        root = root or CONFIG.ABIGALE_ROOT
        self.api = RestAPI(host, port, root)
        if "ABIGALE_USER" in CONFIG and "ABIGALE_PASS" in CONFIG:
            self.login()

    def login(self):
        if not (CONFIG.get("ABIGALE_USER") and CONFIG.get("ABIGALE_PASS")):
            CONFIG.ABIGALE_USER, password = self.prompt_login()
            CONFIG.ABIGALE_PASS = sha256(password)
        self.username = self.api.login(CONFIG.ABIGALE_USER, CONFIG.ABIGALE_PASS)
        return self.username

    @staticmethod
    def prompt_login():
        login_user = getpass.getuser()
        username = input("<Abigale API Login> ({login}):".format(login=login_user))
        username = username or login_user
        password = getpass.getpass("<Password>:")
        return username, password

    @staticmethod
    def _handle(response, *fields):
        if response.status_code == 403:
            raise NotAuthorized()
        elif response.status_code != 200:
            raise Exception("[{}]: {}".format(response.status_code, response.reason))
        response = response.json()
        if response["code"] == 200:
            result = tuple(response.get(field)  for field in fields)
            if len(result) == 1:
                return result[0]
            return result
        elif response["code"] == 403:
            raise exceptions.NotAuthorized(response.get("message"))
        else:
            raise Exception("[{}]: {}".format(response.get("code"), response.get("message")))

    def upload(self, workspace, table, df, metadata=None):
        """
        Upload a DataFrame or Series to the server. The index of the
        data must be DatetimeIndex, because the backend is `arctic` and it
        only supports indexing with datetime.

        Parameters
        ==========
        workspace: str
            workspace to store the data
        table: str
            name of the data
        df: Union[pd.DataFrame, pd.Series]
            the data to upload
        metadata: dict
            metadata to append. Annotate is_backtest=True to indicate this is a backtest
            result. Also, use `permissions` to control the read access to this dataset.
        """
        json_data = DataFrameSerializer.serialize(df, True)
        params = {'metadata': metadata} if metadata else None
        resp = self.api.post("workspace/write/{workspace}/{table}".format(workspace=workspace, table=table), data=json_data, params=params)
        return self._handle(resp)

    def fetch(self, user, workspace, table):
        """
        Fetch a dataset from the server.

        Parameters
        ==========
        user: str
            the owner of the workspace
        workspace: str
            workspace name
        table: str
            dataset name
        
        Returns
        =======
        (data, metadata):
            data is a Series or DataFrame, metadata is a dict.
        """
        resp = self.api.get("workspace/read/{user}/{workspace}/{table}".format(workspace=workspace, table=table, user=user))
        data, metadata = self._handle(resp, "data", "metadata")
        data = DataFrameSerializer.unserialize(data)
        return data, metadata

    def ls(self, username=None, workspace=None):
        """
        list the content of a path. 

        - If both `username` and `workspace` are None, list all the users that owns workspaces;
        - If `username` if given and `workspace` is None, list all workspaces owned by the user;
        - If both are provided, list all the dataset under the workspace owned by the user.]
        """
        path = []
        if username:
            path.append(username)
        if workspace:
            path.append(workspace)
        path = "/".join(path)
        resp = self.api.get("workspace/list", params={"path": path, "requires_metadata": False})
        (items, ) = self._handle(resp, "items")
        return items

