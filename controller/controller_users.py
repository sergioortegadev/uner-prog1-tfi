import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def user_create(dni=None, first_name=None, last_name=None, email=None, user_type=None, curso=None, taller=None, role=None, departament=None):
 if not dni or not first_name or not last_name or not email or not user_type:
  return {
    'message': 'Error: Falta completar algún dato. \n Esta función requiere cinco parámetros.',
    'to_print': {}
  }
 if not isinstance(dni, int):
  return {
   'message': 'Error: El DNI del usuario debe ser un número entero',
   'to_print': {}
  }
 # Simulación de creación de usuario
 # Aquí se podría agregar la lógica para registrar el usuario en una base de datos o sistema
 # Por ahora, simplemente retornamos un mensaje de éxito
 return {
  'message': 'Usuario Creado',
  'to_print': {
   'Id': 1,  
   'DNI': dni,
   'Nombre': first_name,
   'Apellido': last_name,
   'Email': email,
   'Tipo': user_type
  }
 }

def user_update(dni=None):
 if not dni:
  return {
    'message': 'Error: DNI de usuario no proporcionado. \n Esta función requiere el parámetro DNI.',
    'to_print': {}
  }
 if not isinstance(dni, int):
  return {
   'message': 'Error: El DNI del usuario debe ser un número entero',
   'to_print': {}
  }
 # Simulación de actualización de usuario
 # Aquí se podría agregar la lógica para actualizar el usuario en una base de datos o sistema
 # Por ahora, simplemente retornamos un mensaje de éxito
 return {
  'message': 'Usuario Actualizado',
  'to_print': {
   'Id': 1,
   'DNI': dni,
   'Nombre': 'Juan',
   'Apellido': 'Perez',
   'Email': 'nuevo.email@ejemplo.com',
   'Tipo': 'Personal'
  }
 }

def user_delete(dni=None):
 if not dni:
  return {
    'message': 'Error: DNI de usuario no proporcionado. \n Esta función requiere el parámetro DNI.',
    'to_print': {}
  }
 if not isinstance(dni, int):
  return {
   'message': 'Error: El DNI del usuario debe ser un número entero',
   'to_print': {}
  }
 # Simulación de eliminación de usuario
 # Aquí se podría agregar la lógica para eliminar el usuario en una base de datos o sistema
 # Por ahora, simplemente retornamos un mensaje de éxito
 return {
  'message': 'Usuario Eliminado',
  'to_print': {
   'Id': 1,
   'DNI': dni,
   'Nombre': 'Juan',
   'Apellido': 'Perez',
   'Email': 'email@ejemplo.com',
   'Tipo': 'Estudiante'
  }
 }

def user_get_by_dni(dni=None):
 if not dni:
  return {
    'message': 'Error: DNI de usuario no proporcionado. \n Esta función requiere el parámetro DNI.',
    'to_print': {}
  }
 if not isinstance(dni, int):
  return {
   'message': 'Error: El DNI del usuario debe ser un número entero',
   'to_print': {}
  }
 # Simulación de obtención de usuario por DNI
 # Aquí se podría agregar la lógica para obtener el usuario de una base de datos o sistema
 return {
  'message': 'Datos del Usuario',
  'to_print': {
   'Id': 1,
   'DNI': dni,
   'Nombre': 'Juan',
   'Apellido': 'Perez',
   'Email': 'email@ejemplo.com',
   'Tipo': 'Personal'
  }
 }

def user_get_by_name(first_name=None):
 if not first_name:
  return {
    'message': 'Error: Nombre de usuario no proporcionado. \n Esta función requiere el parámetro "name".',
    'to_print': {}
  }
 if not isinstance(first_name, str):
  return {
   'message': 'Error: El nombre del usuario debe ser una cadena de texto',
   'to_print': {}
  }
 # Simulación de obtención de usuario por nombre
 # Aquí se podría agregar la lógica para obtener el usuario de una base de datos o sistema
 return {
  'message': 'Datos del Usuario',
  'to_print': {
   'Id': 1,
   'DNI': 12345678,
   'Nombre': first_name,
   'Apellido': 'Perez',
   'Email': 'email@ejemplo.com',
   'Tipo': 'Estudiante'
  }
 }

def users_list(*args, **kwargs): 
 # Estos parámetros, permite que acepte argumentos opcionales y los ignore. Sin ellos se rompe la ejecución si se le pasa un argumento que no espera.

 # Simulación de listado de usuarios
 # Aquí se podría agregar la lógica para obtener los usuarios de una base de datos o sistema
 # Por ahora, simplemente retornamos un mensaje de éxito con datos simulados
 return {
  'message': 'Listado de Usuarios',
  'to_print': [
   {'Id': 1, 'DNI': 12345678, 'Nombre': 'Juan', 'Apellido': 'Perez', 'Email': 'usuario1@ejemplo.com', 'Tipo': 'Estudiante'},
   {'Id': 2, 'DNI': 87654321, 'Nombre': 'Maria', 'Apellido': 'Gomez', 'Email': 'usuario2@ejemplo.com', 'Tipo': 'Estudiante'},
   {'Id': 3, 'DNI': 11223344, 'Nombre': 'Pedro', 'Apellido': 'Lopez', 'Email': 'usuario3@ejemplo.com', 'Tipo': 'Personal'},
   {'Id': 4, 'DNI': 44332211, 'Nombre': 'Ana', 'Apellido': 'Martinez', 'Email': 'usuario4@ejemplo.com', 'Tipo': 'Personal'}
  ]
}

def users_list_by_type(user_type=None):
    if not user_type:
        return {
            'message': 'Error: Tipo de usuario no proporcionado. \n Esta función requiere el parámetro tipo.',
            'to_print': {}
        }
    if user_type not in ['Estudiante', 'Personal']:
        return {
            'message': 'Error: Tipo de usuario no válido. Debe ser "Estudiante" o "Personal".',
            'to_print': {}
        }
    # Simulación de listado de usuarios por tipo
    # Aquí se podría agregar la lógica para obtener los usuarios de una base de datos o sistema
    return {
        'message': f'Listado de Usuarios por Tipo: {user_type}',
        'to_print': [
            {'Id': 1, 'DNI': 12345678, 'Nombre': 'Juan', 'Apellido': 'Perez', 'Email': 'usuario1@ejemplo.com', 'Tipo': user_type},
            {'Id': 2, 'DNI': 87654321, 'Nombre': 'Maria', 'Apellido': 'Gomez', 'Email': 'usuario2@ejemplo.com', 'Tipo': user_type},
            {'Id': 3, 'DNI': 11223344, 'Nombre': 'Pedro', 'Apellido': 'Lopez', 'Email': 'usuario3@ejemplo.com', 'Tipo': user_type},
            {'Id': 4, 'DNI': 44332211, 'Nombre': 'Ana', 'Apellido': 'Martinez', 'Email': 'usuario4@ejemplo.com', 'Tipo': user_type}
        ]
    } 


# Ejemplo de uso
# print(user_create(12345678, 'Juan', 'Perez', 'usuario1@ejemplo.com', 'Estudiante'))
# print(user_update(12345678))
# print(user_delete(12345678))
# print(user_get_by_dni(12345678))
# print(user_get_by_name('Juan'))
# print(users_list())
# print(users_list('pepe'))
# print(users_list_by_type('Estudiante'))
# print(users_list_by_type('Personal'))
# print(users_list_by_type('Administrador'))  # Esto debería devolver un error
# print(users_list_by_type())  # Esto debería devolver un error
# print(users_list_by_type())  # Esto debería devolver un error
