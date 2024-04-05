from UserRepository import *

class MySQLUserRepository(UserRepository):

    def __init__(self):
        self.user_db_mySql = []

    def get_all(self):
        return self.user_db_mySql
    
    def add(self, user):
        self.user_db_mySql.append(user)