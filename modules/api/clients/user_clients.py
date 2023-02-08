import requests

from modules.common.utils.api_request import APIRequest
from config.config import BASE_URI


class UserClient:
    __TOKEN = 'token'

    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.base_url = BASE_URI + "auth"
        self.request = APIRequest()

    # Send request of authorization on server
    def auth(self, body):
        response = self.request.post(self.base_url, body, self.headers)
        if response.status_code == requests.codes.ok:
            self.headers[UserClient.__TOKEN] = response.as_dict[UserClient.__TOKEN]
        return response
