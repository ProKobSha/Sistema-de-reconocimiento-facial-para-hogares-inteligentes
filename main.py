import os
from register import register_user
from recognize import recognize_user

print("Sistema de inicio de sesión con reconocimiento facial")
print("[1] Registrar usuario")
print("[2] Iniciar sesión")
opcion = input("Selecciona una opción: ")

if opcion == '1':
    nombre = input("Nombre del usuario: ")
    register_user(nombre)
elif opcion == '2':
    recognize_user()
else:
    print("Opción inválida.")
