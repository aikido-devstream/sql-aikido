nombre_usuario = input("Usuario: ")
contrasena = input("Contraseña: ")

query = "SELECT * FROM usuarios WHERE nombre_usuario = '" + nombre_usuario + "' AND contrasena = '" + contrasena + "';"

cursor.execute(query)
