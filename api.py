import requests


class API():
    def __init__(self, token=None):
        self.host = 'http://lifeserver-staging.tocaboca.com/api/v3'
        self.headers = {
            'Authorization': 'Bearer {access_token}'.format(access_token=token)
        }

    def create_account(self, device_id):
        data = {
            "name": "",
            "password": "",
            "email": "",
            "deviceId": device_id
        }
        response = requests.post(
            '{host}/accounts'.format(host=self.host), json=data
        )
        return response

    def authenticaticate_account(self, username, password, device_id):
        data = {
            "identifier": username,
            "password": password,
            "deviceId": device_id,
            "email": "joesparent@example.com",
            "birthdate": "2014-01-03"
        }
        response = requests.post(
            '{host}/accounts/authentication'.format(host=self.host),
            headers=self.headers,
            json=data
        )
        return response
