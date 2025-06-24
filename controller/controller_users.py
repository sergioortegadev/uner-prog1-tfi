from typing import Dict, List, Any, Optional
import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.model_users import create_user, find_user_by_dni, update_user, delete_user, load_users, find_user_by_first_name, find_users_by_user_type


def user_create(dni=None, first_name=None, last_name=None, email=None, user_type=None, curso=None, taller=None, role=None, departament=None):
    if not dni or not first_name or not last_name or not email or not user_type:
        return {
            'message': 'Error: Falta completar algún dato. \n Esta función requiere cinco parámetros.',
            'to_print': {}
        }
    try:
        dni = int(dni)
    except (ValueError, TypeError):
        return {
            'message': 'Error: El DNI del usuario debe ser un número entero',
            'to_print': {}
        }
    try:
        new_user = create_user({
            "nombre": first_name,
            "apellido": last_name,
            "dni": dni,
            "tipo_usuario": user_type,
            "curso": curso,
            "taller": taller,
            "rol": role
        })
        return {
            'message': 'Usuario Creado',
            'to_print': new_user
        }

    except Exception as e:
        return {
            'message': str(e),
            'to_print': {}
        }


def user_update(dni: Optional[int], new_data: Dict[str, Any]):
    if not dni:
        return {
            'message': 'Error: DNI de usuario no proporcionado. \n Esta función requiere el parámetro DNI.',
            'to_print': {}
        }
    user = find_user_by_dni(dni)
    if user is None:
        return {
            'message': 'Error: El usuario con el DNI proporcionado no existe.',
            'to_print': {}
        }

    updated_user = update_user(user["id"], new_data)

    return {
        'message': 'Usuario Actualizado',
        'to_print': updated_user
    }


def user_delete(dni: Optional[int] = None):
    if not dni:
        return {
            'message': 'Error: DNI de usuario no proporcionado. \n Esta función requiere el parámetro DNI.',
            'to_print': {}
        }

    user = find_user_by_dni(dni)
    if user is None:
        return {
            'message': 'Error: El usuario con el DNI proporcionado no existe.',
            'to_print': {}
        }
    has_deleted = delete_user(user['id'])
    if has_deleted:
        return {
            'message': 'Usuario Eliminado',
            'to_print': user
        }


def user_get_by_dni(dni: Optional[int]):
    if not dni:
        return {
            'message': 'Error: DNI de usuario no proporcionado. \n Esta función requiere el parámetro DNI.',
            'to_print': {}
        }
    user = find_user_by_dni(dni)
    if user is None:
        return {
            'message': 'Usuario con el DNI proporcionado no existe.',
            'to_print': {}
        }
    return {
        'message': 'Datos del Usuario',
        'to_print': user
    }


def user_get_by_name(first_name: Optional[str] = None):
    if not first_name or first_name.strip() == '':
        return {
            'message': 'Error: Nombre de usuario no proporcionado. \n Esta función requiere el parámetro "name".',
            'to_print': {}
        }
    user = find_user_by_first_name(first_name)
    if user is None:
        return {
            'message': 'Usuario con el nombre proporcionado no existe.',
            'to_print': {}
        }
    return {
        'message': 'Datos del Usuario',
        'to_print': user
    }


def users_list():
    return {
        'message': 'Listado de Usuarios',
        'to_print': load_users()
    }


def users_list_by_type(user_type: Optional[str] = None):
    if not user_type:
        return {
            'message': 'Error: Tipo de usuario no proporcionado. \n Esta función requiere el parámetro tipo.',
            "to_print": {}
        }
    normalized_user_type = user_type.strip().title()
    if normalized_user_type not in ['Estudiante', 'Personal']:
        return {
            'message': 'Error: Tipo de usuario no válido. Debe ser "Estudiante" o "Personal".',
            'to_print': {}
        }
    return {
        'message': f'Listado de Usuarios por Tipo: {normalized_user_type}',
        'to_print': find_users_by_user_type(normalized_user_type)
    }


# Ejemplo de uso
# print(user_create(12345678, 'Juan', 'Perez', 'usuario1@ejemplo.com', 'Estudiante'))
# print(user_update(12345678))
# print(user_delete(12345678))
# print(user_get_by_dni(22232425))
# print(user_get_by_name('Juan'))
# print(users_list())
# print(users_list('pepe'))
# print(users_list_by_type('Estudiante'))
# print(users_list_by_type('Personal'))
# print(users_list_by_type('Administrador'))  # Esto debería devolver un error
# print(users_list_by_type())  # Esto debería devolver un error
# print(users_list_by_type())  # Esto debería devolver un error
