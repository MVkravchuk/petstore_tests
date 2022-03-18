import re
from model._base_model import BaseModel
from helpers.data_generator import fake


class User(BaseModel):

    def __init__(self, **kwargs):
        self.id: int = kwargs.get('id')
        self.username: str = kwargs.get('username')
        self.firstName: str = kwargs.get('first_name')
        self.lastName: str = kwargs.get('last_name')
        self.email: str = kwargs.get('email')
        self.password: str = kwargs.get('password')
        self.phone: str = kwargs.get('phone')
        self.userStatus: int = kwargs.get('user_stasus')

    def generate(self, **kwargs):
        self.id: int = kwargs.get('id', fake.bothify(text='#######'))
        self.username: str = kwargs.get('username', fake.word())
        self.firstName: str = kwargs.get('first_name', fake.first_name())
        self.lastName: str = kwargs.get('last_name', fake.last_name())
        self.email: str = kwargs.get('email', fake.email())
        self.password: str = kwargs.get('password', fake.word())
        self.phone: str = kwargs.get('phone', fake.phone_number())
        self.userStatus: int = kwargs.get('user_stasus', fake.bothify(text='#######'))
        return self
