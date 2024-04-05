from User import *

class UserService:

    def __init__(self, repository):
        self.repository = repository
        
        
    def get_all_users(self):
        return self.repository.get_all()


    def add_user(self, user):
        self.repository.add(user)


    def create_user(self, name, username, email):
        #user = User(name, username, email)   // CODE SMELL
        self.repository.add(User(name, username, email))