import requests


class HttpClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def get(self, url):
        params = {'access_token': self.token}
        response = requests.get(self.base_url + url, params=params)
        return response

    def post(self, url, data):
        params = {'access_token': self.token}
        response = requests.post(self.base_url + url, params=params, data=data)
        return response
