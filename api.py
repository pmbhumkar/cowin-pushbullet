import requests
import json


class APIClient(object):
    def __init__(self):
        self.base_url = "https://cdn-api.co-vin.in/api"


    def session(self):
        self.s = requests.Session()


    def get(self, method, params=None):
        response = self.s.get(self.base_url + method, params=params, verify=False)
        return (response.text, response.status_code)