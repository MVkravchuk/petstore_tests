import requests


class ApiService(object):

    def __init__(self, base_url: str = 'https://petstore.swagger.io/v2'):
        self.base_url: str = base_url

class UserApiService(ApiService):

    def __init__(self):
        super().__init__()
        self.base_url = self.base_url + '/user'

    
    def create_user(self, user: dict):
        return requests.post(self.base_url, json=user).json()
    
    def get_user_by_username(self, username: str) -> dict:
        return requests.get(self.base_url + f'/{username}').json()

    def delete_user(self, username:str):
        return requests.delete(self.base_url + f'/{username}')
