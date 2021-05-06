import requests
import json

from fake_headers import Headers


class APIClient(object):
    def __init__(self):
        self.base_url = "https://cdn-api.co-vin.in/api"
        self.headers = Headers(
            browser="chrome",
            os="win",
            headers=True
        )

    def session(self):
        self.s = requests.Session()


    def get(self, method, params=None):
        response = self.s.get(self.base_url + method, params=params,
            verify=False, headers=self.headers.generate())
        return (response.text, response.status_code)