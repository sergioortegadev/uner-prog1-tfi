from typing import Dict, List, Any, Optional
from datetime import datetime
from model.model_data import load_json_file, save_json_file
from model.new_id import new_id
# from model.model_tools import find_tool_by_id, update_tool, ToolType, ToolStatus
from enum import Enum

FILE = "maintenance.json"
# REQUIRED_MAINTENANCE_FIELDS = ["id_tool",
#                                "maintenance_type", "description", "responsible"]


# class MaintenanceType(Enum):
#     PREVENTIVO = "Preventivo"
#     CORRECTIVO = "Correctivo"


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


# def find_maintenance_index_by_id(records: List[Dict[str, Any]], maintenance_id: int) -> int:
#     """
#     Buscar índice de mantenimiento por ID.

#     Args:
#         records (List[Dict[str, Any]]): Lista de registros de mantenimiento.
#         maintenance_id (int): ID del mantenimiento a buscar.

#     Returns:
#         int: Índice del mantenimiento si se encuentra, -1 en caso contrario.
#     """
#     for i, record in enumerate(records):
#         if record["id"] == maintenance_id:
#             return i
#     return -1


# def complete_maintenance(maintenance_id: int, tool_status: str = ToolStatus.DISPONIBLE.value) -> Dict[str, Any]:
#     """Marcar mantenimiento como completado y actualizar estado de la herramienta.

#     La función actualiza el estado de la herramienta a "Disponible" (o un estado
#     especificado) y agrega la fecha de finalización del mantenimiento.

#     Args:
#         maintenance_id (int): ID del mantenimiento a completar.
#         tool_status (str): Estado a asignar a la herramienta (default: "Disponible").

#     Returns:
#         Dict[str, Any]: El registro de mantenimiento actualizado.
#     Raises:
#         ValueError:  Si no se encuentra el mantenimiento con el ID especificado o  Si el registro de mantenimiento no contiene un 'id_herramienta'.
#     """
#     records = load_maintenance()
#     record_index = find_maintenance_index_by_id(records, maintenance_id)
#     if record_index == -1:
#         raise ValueError(
#             f"Mantenimiento con ID {maintenance_id} no encontrado")

#     # Actualizar estado de la herramienta
#     tool_id = records[record_index].get("id_herramienta")
#     if tool_id is None:
#         raise ValueError(
#             "El registro de mantenimiento no contiene un 'id_herramienta'")
#     update_tool(tool_id, {"estado": tool_status})
#     # Usar la misma marca de tiempo para consistencia
#     records[record_index]["fecha_mantenimiento"] = datetime.now().isoformat()
#     save_maintenance(records)
#     return records[record_index]


# def get_tool_maintenance(tool_id: int) -> List[Dict[str, Any]]:
#     """Obtener historial de mantenimiento de una herramienta.

#     La función devuelve una lista con todos los registros de mantenimiento de una herramienta con el ID especificado.

#     Args:
#         tool_id (int): ID de la herramienta a buscar.

#     Returns:
#         List[Dict[str, Any]]: Lista de registros de mantenimiento.
#     """
#     records = load_maintenance()
#     # Filtrar registros de mantenimiento por herramienta
#     return [record for record in records if record["id_herramienta"] == tool_id]
