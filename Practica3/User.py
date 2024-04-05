class User:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    def __str__(self) -> str:
        return "Nombre: " + self.name + " UserName: " + self.username + " Correo: " + self.email