from model.model_users import create_user, find_user_by_dni, update_user, delete_user,  find_user_by_first_name, find_users_by_user_type, load_users
from typing import Dict, List, Any, Optional
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def user_create(dni=None, datos_usuario: Optional[Dict[str, Any]] = None, first_name: Optional[str] = None, last_name: Optional[str] = None, email: Optional[str] = None, user_type: Optional[str] = None, curso: Optional[str] = None, taller: Optional[str] = None, role: Optional[str] = None, dep: Optional[str] = None):
    if not dni or not first_name or not last_name or not email or not user_type:
        return {
            'message': 'Error: Falta completar algún dato. \n Esta función requiere cinco parámetros.',
            'to_print': {}
        }
    try:
        dni = int(dni)
        if find_user_by_dni(dni):
            return {
                'message': 'Error: Ya existe un usuario registrado con ese DNI.',
                'to_print': {}
            }

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
            "email": email,
            "tipo_usuario": user_type,
            "curso": curso,
            "taller": taller,
            "rol": role,
            "dep": dep,
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


def user_update(dni: Optional[int], datos_usuario: Optional[Dict[str, Any]] = None, first_name: Optional[str] = None, last_name: Optional[str] = None, email: Optional[str] = None, user_type: Optional[str] = None, curso: Optional[str] = None, taller: Optional[str] = None, role: Optional[str] = None, dep: Optional[str] = None):
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

    data_new = {
        "nombre": first_name,
        "apellido": last_name,
        "dni": dni,
        "email": email,
        "tipo_usuario": user_type,
        "curso": curso,
        "taller": taller,
        "rol": role,
        "dep": dep,
    }

    updated_user = update_user(user["id"], data_new)

    return {
        'message': 'Usuario Actualizado',
        'to_print': updated_user
    }


def user_delete(dni: Optional[int] = None):
    if not dni:
        return {
            'message': 'Error: DNI de usuario no proporcionado.',
            'to_print': {}
        }

    user = find_user_by_dni(dni)
    if user is None:
        return {
            'message': 'Error: El usuario con el DNI proporcionado no existe.',
            'to_print': {}
        }
    # Confirmación de eliminación
    confirmation = input(
        f"¿Estás seguro de que deseas eliminar al usuario ? (s/n): ").strip().lower()
    if confirmation != 's':
        return {
            'message': 'Operación cancelada. El usuario no ha sido eliminado.',
            'to_print': {}
        }

    # Eliminacion de usuario
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


def user_get_by_name(partial_name: Optional[str] = None):
    if not partial_name or partial_name.strip() == '':
        return {
            'message': 'Error: Nombre de usuario no proporcionado. Esta función requiere el parámetro "name".',
            'to_print': {}
        }

    matches = find_user_by_first_name(partial_name.strip())

    if not matches:
        return {
            'message': 'Usuario con el nombre proporcionado no existe.',
            'to_print': {}
        }

    return {
        'message': f'Se encontraron {len(matches)} coincidencia(s).',
        'to_print': matches
    }


def users_list():
    users = load_users()
    return {
        'message': 'Listado de Usuarios' if users else 'No hay usuarios registrados.',
        'to_print': users if users else []
    }


def users_list_by_type(user_type: Optional[str] = None):
    if not user_type:
        return {
            'message': 'Error: Tipo de usuario no proporcionado. \n Esta función requiere el parámetro tipo.',
            "to_print": {}
        }
    normalized_user_type = user_type.strip().title()
    if normalized_user_type not in ['1', '2']:
        return {
            'message': 'Error: Tipo de usuario no válido. Debe ser "1" para Estudiante o "2" para Personal.',
            'to_print': {}
        }
    return {
        'message': f'Listado de Usuarios por Tipo: {'Estudiante' if normalized_user_type == '1'else 'Personal'}',
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
