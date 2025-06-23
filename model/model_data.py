import json
import os
from pathlib import Path
from typing import Dict, List, Any, Union, Optional


DATA_DIR = Path(os.path.join(os.path.dirname(
    os.path.dirname(__file__)), 'data'))


def ensure_data_dir() -> None:
    """Asegura que el directorio de 'data' existe
    Crea el directorio 'data' si aún no existe.
    """
    if not DATA_DIR.exists():
        DATA_DIR.mkdir(parents=True, exist_ok=True)


def load_json_file(file_name: str, default_data: Optional[Any] = None) -> list[dict[str, Any]]:
    """Carga datos desde un archivo JSON

    Args:
        file_name: Nombre del archivo JSON a cargar (sin ruta de directorio)
        default_data: Datos por defecto a devolver si el archivo no existe

    Raises:
        IOError: Si hay un error al cargar el archivo JSON

    """
    ensure_data_dir()
    file_path = DATA_DIR / file_name

    # Devuelve los datos por defecto si el archivo no existe
    if not file_path.exists() and default_data is not None:
        return default_data

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        raise IOError(f"Error al cargar el archivo {file_name}: {str(e)}")


def save_json_file(file_name: str, data: Any):
    """Guarda datos en un archivo JSON

    Args:
        file_name: Nombre del archivo JSON a guardar (sin ruta de directorio)
        data: Datos a guardar en el archivo JSON
    Raises:
        IOError: Si hay un error al guardar el archivo JSON

    """
    ensure_data_dir()
    file_path = DATA_DIR / file_name

    try:
        # Abre el archivo y guarda los datos en formato JSON
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        raise IOError(f"Error al guardar el archivo {file_name}: {str(e)}")


def get_next_id(items: List[Dict[str, Any]]) -> int:
 if not items:
     return 1
 
 max_id = max(item.get('id', 0) for item in items)
 return max_id + 1 if max_id > 0 else 1

