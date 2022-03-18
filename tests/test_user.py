from helpers.servise import UserApiService

class TestCreateUser:

    def test_can_create_new_user(self, new_user):
        response = UserApiService().create_user(new_user)
        assert response["code"] == 200
