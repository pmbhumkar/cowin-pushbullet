import requests
import json


class APIClient(object):
    def __init__(self):
        self.base_url = "https://cdn-api.co-vin.in/api"
        self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"}

    def session(self):
        self.s = requests.Session()


    def get(self, method, params=None):
        response = self.s.get(self.base_url + method, params=params, verify=False, headers=self.headers)
        return (response.text, response.status_code)