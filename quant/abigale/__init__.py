import getpass
from ..common.settings import CONFIG
from .api import RestAPI
from .exceptions import NotAuthorized
from .serializers import DataFrameSerializer
from .security import sha256


class Abigale:
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
            return [response.get(field)  for field in fields]
        elif response["code"] == 403:
            raise NotAuthorized(response.get("message"))
        else:
            raise Exception("[{}]: {}".format(response.get("code"), response.get("message")))

    def upload(self, workspace, table, df, metadata=None):
        json_data = DataFrameSerializer.serialize(df, True)
        params = {'metadata': metadata} if metadata else None
        resp = self.api.post("workspace/write/{workspace}/{table}".format(workspace=workspace, table=table), data=json_data, params=params)
        return self._handle(resp)

    def fetch(self, user, workspace, table):
        resp = self.api.get("workspace/read/{user}/{workspace}/{table}".format(workspace=workspace, table=table, user=user))
        data, metadata = self._handle(resp, "data", "metadata")
        data = DataFrameSerializer.unserialize(data)
        return data, metadata

    def ls(self, username=None, workspace=None):
        path = []
        if username:
            path.append(username)
        if workspace:
            path.append(workspace)
        path = "/".join(path)
        resp = self.api.get("workspace/list", params={"path": path, "requires_metadata": False})
        (items, ) = self._handle(resp, "items")
        return items
