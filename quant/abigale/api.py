import base64
import requests
import urllib
from quant.common.settings import CONFIG


class TokenAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, req):
        req.headers["Authorization"] = "Token {}".format(self.token)
        return req


class APIMethod:
    def __init__(self, method):
        self.method = method

    def __get__(self, obj, type=None):
        if type is None:
            return self
        def request(uri, *args, **kwargs):
            url = urllib.parse.urljoin(obj.root_url, uri)
            req = getattr(obj.session, self.method)(url, *args, auth=obj.auth, **kwargs)
            return req
        return request


class RestAPI:
    get    = APIMethod("get")
    post   = APIMethod("post")
    put    = APIMethod("put")
    delete = APIMethod("delete")

    def __init__(self, host=None, port=None, root=None):
        self.root_url = "http://{host}:{port}/{root}".format(host=host, port=port, root=root)
        self.auth = None
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Abigale API",
            "Content-Type": "application/json",
        })

    def login(self, username, password):
        # self.session.headers["Authorization"] = "basic " + base64.b64encode("{}:{}".format(self.username, self.password).encode("utf8")).decode("utf8")
        self.auth = requests.auth.HTTPBasicAuth(username, password)
        return self.get("/users/whoami").json().get("username")

    def login_with_token(self, token):
        self.auth = TokenAuth(token)
