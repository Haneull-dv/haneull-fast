from com.haneull.auth.user.web.user_factory import UserFactory


class UserController:

    def __init__(self):
        pass

    def hello_user(self, **kwargs):
        return UserFactory.create(strategy="hello_user", **kwargs)
