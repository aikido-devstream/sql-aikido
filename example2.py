nombre_usuario = input("Usuario: ")
contrasena = input("Contraseña: ")

query = "SELECT * FROM usuarios WHERE nombre_usuario = %s AND contrasena = %s;"
cursor.execute(query, (nombre_usuario, contrasena))
