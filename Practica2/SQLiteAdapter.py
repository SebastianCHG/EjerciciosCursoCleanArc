import sqlite3

class SQLiteAdapter:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def conectar(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def crear_tabla_usuarios(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                email TEXT NOT NULL,
                contraseña TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def insertar_usuario(self, nombre, email, contraseña):
        self.cursor.execute('''
            INSERT INTO usuarios (nombre, email, contraseña)
            VALUES (?, ?, ?)
        ''', (nombre, email, contraseña))
        self.connection.commit()

# Ejemplo de uso:
adaptador_sqlite = SQLiteAdapter('bd_user.db')
adaptador_sqlite.conectar()
adaptador_sqlite.crear_tabla_usuarios()

# Insertar un nuevo usuario
adaptador_sqlite.insertar_usuario("Luisa Fernanda Escobar", "luisamarquez2008@gmail.com", "password123")