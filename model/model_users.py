import re
from typing import Dict, List, Any, Optional
from model.model_data import load_json_file, save_json_file
from model.new_id import new_id

FILE = "users.json"
REQUIRED_USER_FIELDS = ["nombre", "dni", "apellido", "tipo_usuario"]


def load_users() -> List[Dict[str, Any]]:
    return load_json_file(FILE, default_data=[])


def save_users(users: List[Dict[str, Any]]):
    save_json_file(FILE, users)


def validate_dni(dni: str, users: List[Dict[str, Any]], exclude_id: Optional[int] = None) -> None:
    if not re.match(r'^\d{8}$', dni):
        raise ValueError(
            f"DNI '{dni}'. El DNI debe tener exactamente 8 dígitos")

    for user in users:
        if user["dni"] == dni and (exclude_id is None or user["id"] != exclude_id):
            raise ValueError(f"DNI '{dni}' Ya existe un usuario con este DNI")


def create_user(user_data: Dict[str, Any]) -> Dict[str, Any]:

    users = load_users()

    for field in REQUIRED_USER_FIELDS:
        if field not in user_data:
            raise ValueError(f"El campo {field} es obligatorio")

    new_user = {
        "id": new_id(users),
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


def find_user_by_dni(dni: int) -> Optional[Dict[str, Any]]:
    users = load_users()
    for user in users:
        if user["dni"] == dni:
            return user
    return None


def find_user_by_first_name(first_name: str) -> List[Dict[str, Any]]:
    users = load_users()
    return [
        user for user in users
        if 'nombre' in user and first_name.lower() in user['nombre'].lower()
    ]


def find_users_by_user_type(user_type: str) -> List[Dict[str, Any]]:
    user_type_text = 'Estudiante' if user_type == '1' else 'Personal'
    users = load_users()
    return [user for user in users if user["tipo_usuario"].lower() == user_type_text.lower()]


def find_user_by_id(user_id: int) -> Optional[Dict[str, Any]]:
    users = load_users()
    for user in users:
        if user["id"] == user_id:
            return user
    return None


def find_user_index_by_id(user_id: int, users: List[Dict[str, Any]]) -> int:
    for i, user in enumerate(users):
        if user["id"] == user_id:
            return i
    return -1


def update_user(user_id: int, user_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    users = load_users()

    user_index = find_user_index_by_id(user_id, users)
    updated_user = users[user_index].copy()
    for key, value in user_data.items():
        if key != "id":
            updated_user[key] = value

    users[user_index] = updated_user
    save_users(users)

    return updated_user


def delete_user(user_id: int) -> bool:
    users = load_users()
    user_index = find_user_index_by_id(user_id, users)

    if user_index == -1:
        return False

    users.pop(user_index)
    save_users(users)

    return True
