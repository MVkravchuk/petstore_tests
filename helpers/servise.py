import requests

from model.user_model import User


class ApiService(object):

    def __init__(self):
        pass

class UserApiService(ApiService):

    def __init__(self):
        super().__init__()
        pass 
    
    def create_user(self, user: dict | User):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }
        if type(user) == User:
            user = user.to_dict()
        return requests.post('https://petstore.swagger.io/v2/user', headers=headers, json=user).json()