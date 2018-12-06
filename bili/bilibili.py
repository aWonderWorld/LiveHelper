import aiohttp

import requests
from configLoader import ConfigLoader

class Bilibili():
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Bilibili, cls).__new__()
            dictAccount = ConfigLoader().dictAccount
            cls.instance.dictAccount = dictAccount
            cls.instance.var_bili_session = None
            cls.instance.var_other_session = None
            cls.instance.var_login_session = None
            cls.instance.app_params = f'actionKey={dictAccount["actionKey"]}&appkey={dictAccount["appkey"]}&build={dictAccount["build"]}&device={dictAccount["device"]}&mobi_app={dictAccount["mobi_app"]}&platform={dictAccount["platform"]}'
        return cls.instance

    @property
    def login_session(self):
        if self.login_session is None:
            self.login_session = requests.Session()
        return self.login_session

    @property
    def bili_session(self):
        if self.bili_session is None:
            self.bili_session = aiohttp.ClientSession()
        return self.bili_session

