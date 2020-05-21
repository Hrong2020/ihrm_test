import requests


class TestLoginApi:
    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"

    def login(self, jsonData, headers):
        response = requests.post(url=self.login_url,
                                     json=jsonData,
                                     headers=headers)
        return response


