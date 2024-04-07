from User import *

class UserUseCase:

    def crear_usuario(user_id, nombre, email, contraseña):
        usuario = User(user_id, nombre, email, contraseña)
        return usuario
