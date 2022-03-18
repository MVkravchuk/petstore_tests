from model.user_model import User
import pytest

@pytest.fixture(scope="function")
def new_user() -> User:
    return User().create()
