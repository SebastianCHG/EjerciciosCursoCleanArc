from UserService import *
from User import *
from MySQLUserRepository import *
from UserController import *

mySQLUserRepository = MySQLUserRepository()
userService = UserService(mySQLUserRepository)
userController = UserController(userService)

userController.create_user('Sebastian', 'schavar', 'schavar@gmail.com')
userController.create_user('Juan Pablo', 'jpbecerr', 'jpbecerr@gmail.com')
userController.get_all_users()