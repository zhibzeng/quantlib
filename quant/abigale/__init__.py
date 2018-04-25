"""
quant.abigale is a python module that supports Abigale Project.
It was originally part of the Abigale Project called AbiClient.
It helps upload timeseries data and backtest results to servers.
"""
import json
import getpass
from ..common.settings import CONFIG
from ..common.logging import Logger
from .api import RestAPI
from .serializers import DataFrameSerializer
from .security import sha256
from . import api, exceptions


__all__ = ['RestAPI', 'exceptions', 'sha256', 'api']


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
            raise exceptions.NotAuthorized()
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

    def ls(self, path):
        data = self._handle(self.api.get('/files/ls', params={'path': path}), 'data')
        return data

    def create_strategy(self, path, name, data):
        """
        Create a new strategy file named `name` under `path` with `data`
        """
        status = self._handle(self.api.post('files/new', params={'path': path, 'name': name}, data=data), 'status')
        return status

