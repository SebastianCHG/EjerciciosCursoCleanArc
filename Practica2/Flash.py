from flask import Flask, request, jsonify
from SQLiteAdapter import SQLiteAdapter
from UserUseCase import crear_usuario

app = Flask(__name__)

adaptador_sqlite = SQLiteAdapter('bd_user.db')
adaptador_sqlite.conectar()

# Ruta para crear un usuario
@app.route('/usuarios', methods=['POST'])
def crear_usuario_route():
    data = request.json
    user_id = data.get('id')
    nombre = data.get('nombre')
    email = data.get('email')
    contraseña = data.get('contraseña')

    if not user_id or not nombre or not email or not contraseña:
        return jsonify({'error': 'Faltan datos'}), 400

    nuevo_usuario = crear_usuario(user_id, nombre, email, contraseña)
    adaptador_sqlite.insertar_usuario(nombre, email, contraseña)

    return jsonify({'msg': 'Usuario creado'}), 200
