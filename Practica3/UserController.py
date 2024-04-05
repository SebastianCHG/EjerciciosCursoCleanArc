class UserController:

    def __init__(self, user_service):
        self.user_service = user_service

    def get_all_users(self):
        listUser = self.user_service.get_all_users()

        for user in listUser:
            print(user)

    def create_user(self, name, username, email):
        self.user_service.create_user(name, username, email)
