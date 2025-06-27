from typing import Dict, List, Any, Optional
from datetime import datetime
from model.model_data import load_json_file, save_json_file
from model.new_id import new_id
from enum import Enum

FILE = "maintenance.json"


def load_maintenance() -> List[Dict[str, Any]]:
    """Cargar registros de mantenimiento desde el archivo JSON"""
    return load_json_file(FILE, [])


def save_maintenance(data: List[Dict[str, Any]]) -> None:
    """Guardar registros de mantenimiento en el archivo JSON"""
    save_json_file(FILE, data)


def create_maintenance(maintenance_data: Dict[str, Any]) -> Dict[str, Any]:
   
    maintenance = load_maintenance()

    new_record = {
        "id": new_id(maintenance),
        "tool_id": maintenance_data["tool_id"],
        "herramienta": maintenance_data["herramienta"],
        "fecha": maintenance_data["fecha"],
        "tipo": maintenance_data["tipo"],
        "descripcion": maintenance_data["descripcion"],
        "responsable": maintenance_data["responsable"],
        "costo": maintenance_data["costo"],
        "siguiente": maintenance_data["siguiente"]
    }

    maintenance.append(new_record)
    save_maintenance(maintenance)
    return new_record

