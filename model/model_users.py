import re
from typing import Dict, List, Any, Optional

from models.data import load_json_file, save_json_file,  get_next_id

USERS_FILE = "usuarios.json"
REQUIRED_USER_FIELDS = ["nombre", "dni", "apellido", "tipo_usuario"]


def load_users() -> List[Dict[str, Any]]:
    """
    Carga la lista de usuarios desde el archivo JSON.

    Returns:
        Lista de diccionarios de usuarios.
    """
    return load_json_file(USERS_FILE, default_data=[])


def save_users(users: List[Dict[str, Any]]) -> bool:
    """
    Guarda la lista de usuarios en el archivo JSON.

    Args:
        users: Lista de diccionarios de usuarios a guardar.
    """
    return save_json_file(USERS_FILE, users)


def validate_dni(dni: str, users: List[Dict[str, Any]], exclude_id: Optional[int] = None) -> None:
    """Valida el formato y unicidad del DNI

    Args:
        dni: DNI a validar
        users: Lista de usuarios existentes para buscar duplicados
        exclude_id: ID del usuario a excluir de la búsqueda de duplicados (para ediciones)

    Raises:
        ValueError: Si el DNI es inválido o duplicado
    """
    # Verificar formato DNI (8 dígitos)
    if not re.match(r'^\d{8}$', dni):
        raise ValueError(
            f"DNI '{dni}'. El DNI debe tener exactamente 8 dígitos")

    # Verificar unicidad
    for user in users:
        if user["dni"] == dni and (exclude_id is None or user["id"] != exclude_id):
            raise ValueError(f"DNI '{dni}' Ya existe un usuario con este DNI")


def create_user(user_data: Dict[str, Any]) -> Dict[str, Any]:
    """Crea un nuevo usuario

    Args:
        user_data: Diccionario con los datos del usuario a crear

    Returns:
        Diccionario del usuario creado con su ID

    Raises:
        ValueError: Si falta algún campo requerido o la validación falla
    """
    # Cargar usuarios existentes
    users = load_users()

    for field in REQUIRED_USER_FIELDS:
        if field not in user_data:
            raise ValueError(f"El campo {field} es obligatorio")

    # Verificar DNI
    validate_dni(user_data["dni"], users)

    new_user = {
        "id": get_next_id(users),
        "nombre": user_data["nombre"],
        "apellido": user_data["apellido"],
        "dni": user_data["dni"],
        "tipo_usuario": user_data["tipo_usuario"],
    }

    for key, value in user_data.items():
        if key not in new_user and key != "id":
            new_user[key] = value

    users.append(new_user)
    save_users(users)

    return new_user


def find_user_by_dni(dni: str) -> Optional[Dict[str, Any]]:
    """Buscar un usuario por DNI

    Args:
        dni: DNI del usuario a buscar

    Returns:
        Diccionario del usuario si se encuentra, None en caso contrario
    """
    users = load_users()
    for user in users:
        if user["dni"] == dni:
            return user
    return None


def find_user_by_id(user_id: int) -> Optional[Dict[str, Any]]:
    """Buscar un usuario por ID

    Args:
        user_id: ID del usuario a buscar

    Returns:
        Diccionario del usuario si se encuentra, None en caso contrario
    """
    users = load_users()
    for user in users:
        if user["id"] == user_id:
            return user
    return None


def find_user_index_by_id(user_id: int, users: List[Dict[str, Any]]) -> int:
    """Buscar índice de usuario por ID

    Args:
        user_id: ID del usuario a buscar
        users: Lista de usuarios

    Returns:
        Índice del usuario si se encuentra, -1 en caso contrario
    """

    for i, user in enumerate(users):
        if user["id"] == user_id:
            return i
    return -1


def update_user(user_id: int, user_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Actualizar un usuario existente

    Args:
        user_id: ID del usuario a actualizar
        user_data: Diccionario con los nuevos datos del usuario

    Returns:
        Diccionario del usuario actualizado si se encuentra, None en caso contrario

    Raises:
        InvalidDataError: Si la validación falla
    """
    users = load_users()

    # Encontrar índice del usuario
    user_index = find_user_index_by_id(user_id, users)

    if user_index == -1:
        raise ValueError(f"Usuario con ID {user_id} no encontrado")

    # Validar DNI  si se proporciona
    if "dni" in user_data:
        validate_dni(user_data["dni"], users, exclude_id=user_id)

    # Actualizar usuario
    updated_user = users[user_index].copy()
    for key, value in user_data.items():
        if key != "id":
            updated_user[key] = value

    users[user_index] = updated_user
    save_users(users)

    return updated_user


def delete_user(user_id: int) -> bool:
    """Eliminar un usuario

    Args:
        user_id: ID del usuario a eliminar

    Returns:
        True si el usuario se eliminó, False si no se encontró
    """
    users = load_users()
    # Encontrar índice del usuario
    user_index = find_user_index_by_id(user_id, users)

    if user_index == -1:
        return False

    users.pop(user_index)
    save_users(users)

    return True
