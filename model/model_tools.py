from typing import Dict, List, Any, Optional
from model.model_data import load_json_file, save_json_file
from model.new_id import new_id
from enum import Enum

FILE = "tools.json"


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
