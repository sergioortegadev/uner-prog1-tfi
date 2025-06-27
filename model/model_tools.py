from typing import Dict, List, Any, Optional
from model.model_data import load_json_file, save_json_file
from model.new_id import new_id
from enum import Enum
from model.model_data import load_json_file, save_json_file

FILE = "tools.json"
REQUIRED_TOOL_FIELDS = ["nombre", "tipo", "ubicacion"]


class ToolStatus(Enum):
    DISPONIBLE = "Disponible"
    EN_USO = "En uso"
    EN_MANTENIMIENTO = "En mantenimiento"
    FUERA_DE_SERVICIO = "Fuera de servicio"


class ToolType(Enum):
    HERRAMIENTA_MANUAL = "Herramienta Manual"
    MAQUINA_ELECTRICA = "Máquina Eléctrica"
    HERRAMIENTA_ELECTRICA = "Herramienta Eléctrica"
    CONSUMIBLE = "Consumible"


def load_tools() -> List[Dict[str, Any]]:
    return load_json_file(FILE, [])


def save_tools(tools: List[Dict[str, Any]]) -> None:
    save_json_file(FILE, tools)



def create_tool(new_tool: Dict[str, Any]) -> Dict[str, Any]:
    
    tools = load_tools()

    new_tool = {
        "id": new_id(tools),
        "nombre": new_tool["nombre"],
        "tipo": new_tool["tipo"],
        "marca": new_tool.get("marca", ""),
        "modelo": new_tool.get("modelo", ""),
        "estado": new_tool["estado"],
        "ubicacion": new_tool["ubicacion"],
        "observaciones": new_tool.get("observaciones", ""),
        "disponible": True,
    }

    tools.append(new_tool)
    save_tools(tools)
    return new_tool
