from typing import Dict, List, Any, Optional
#from models.data import get_next_id, load_json_file, save_json_file
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
    """Cargar herramientas desde el archivo JSON"""
    return load_json_file(FILE, [])


def save_tools(tools: List[Dict[str, Any]]) -> None:
    """Guardar herramientas en el archivo JSON"""
    save_json_file(FILE, tools)


# def validate_tool_type(tool_type: str) -> None:
#     """Validar tipo de herramienta

#     Args:
#         tool_type (str): Tipo de herramienta a validar

#     Raises:
#         ValueError: Si el tipo no es válido
#     """
#     if tool_type not in [t.value for t in ToolType]:
#         raise ValueError(
#             f"Tipo de herramienta inválido. Debe ser uno de: {', '.join([t.value for t in ToolType])}")


# def validate_tool_status(status: str) -> None:
#     """
#     Validar estado de herramienta

#     Args:
#         status (str): Estado de la herramienta a validar

#     Raises:
#         ValueError: Si el estado no es válido
#     """
#     if status not in [s.value for s in ToolStatus]:
#         raise ValueError(
#             f"Estado inválido. Debe ser uno de: {', '.join([s.value for s in ToolStatus])}")


# def create_tool(tool_data: Dict[str, Any]) -> Dict[str, Any]:
#     """Crear nueva herramienta

#     La herramienta se crea con los campos obligatorios y los campos opcionales
#     que se hayan proporcionado. El estado se setea en "Disponible" si no se
#     proporciona.

#     Args:
#         tool_data (Dict[str, Any]): Diccionario con los campos de la herramienta

#     Returns:
#         Dict[str, Any]: Diccionario de la herramienta recién creada
#     Raises:
#         ValueError: Si faltan campos obligatorios o si el tipo/estado no es válido
#     """
#     tools = load_tools()

#     # Validar campos requeridos
#     for field in REQUIRED_TOOL_FIELDS:
#         if not tool_data.get(field):
#             raise ValueError(f"El campo {field} es obligatorio")

#     # Validar tipo y estado
#     if "tipo" in tool_data:
#         validate_tool_type(tool_data["tipo"])
#         if "estado" in tool_data and tool_data["estado"] is not None:
#             validate_tool_status(tool_data["estado"])
#         validate_tool_status(tool_data.get("estado"))

#     new_tool = {
#         "id": get_next_id(tools),
#         "nombre": tool_data["nombre"],
#         "tipo": tool_data["tipo"],
#         "estado": tool_data.get("estado", ToolStatus.DISPONIBLE.value),
#         "ubicacion": tool_data["ubicacion"]
#     }

#     # Agregar campos opcionales
#     OPTIONAL_FIELDS = ["marca", "modelo",
#                        "numero_serie", "fecha_adquisicion", "notas"]
#     for field in OPTIONAL_FIELDS:
#         if field in tool_data:
#             new_tool[field] = tool_data[field]

#     # Guardar la herramienta en la base de datos
#     tools.append(new_tool)
#     save_tools(tools)
#     return new_tool


# def find_tool_by_id(tool_id: int) -> Optional[Dict[str, Any]]:
#     """
#     Busca una herramienta por su ID único y devuelve su diccionario

#     Args:
#         tool_id (int): ID de la herramienta a buscar

#     Returns:
#         Optional[Dict[str, Any]]: Diccionario de la herramienta si se encuentra,
#             None en caso contrario
#     """
#     tools = load_tools()
#     for tool in tools:
#         if tool["id"] == tool_id:
#             return tool
#     return None


# def find_tool_by_name(name: str) -> List[Dict[str, Any]]:
#     """

#     Busca herramientas cuyo nombre contiene el texto proporcionado

#     Args:
#         name (str): Texto a buscar en el nombre

#     Returns:
#         List[Dict[str, Any]]: Lista de herramientas que coinciden con la búsqueda
#     """
#     # Cargar lista de herramientas
#     tools = load_tools()
#     # Iterar sobre la lista para encontrar herramientas que coinciden
#     return [tool for tool in tools if name.lower() in tool["nombre"].lower()]


# def find_tool_index_by_id(tools: List[Dict[str, Any]], tool_id: int) -> int:
#     """
#     Buscar índice de herramienta por ID

#     Args:
#         tools: Lista de herramientas
#         tool_id: ID de la herramienta a buscar

#     Returns:
#         Índice de la herramienta si se encuentra, -1 en caso contrario
#     """
#     # Iterar sobre la lista de herramientas para encontrar el índice
#     for i, tool in enumerate(tools):
#         if tool["id"] == tool_id:
#             return i
#     return -1


# def update_tool(tool_id: int, tool_data: Dict[str, Any]) -> Dict[str, Any]:
#     """
#     Actualizar herramienta existente

#     La función carga la lista de herramientas, encuentra la herramienta que
#     coincide con el ID proporcionado y actualiza los campos proporcionados.

#     Args:
#         tool_id (int): ID de la herramienta a actualizar
#         tool_data (Dict[str, Any]): Diccionario con los campos a actualizar

#     Returns:
#         Dict[str, Any]: Diccionario con la herramienta actualizada

#     Raises:
#         ValueError: Si no se encuentra la herramienta con el ID proporcionado o
#             Si el tipo o estado de la herramienta no es válido
#     """
#     tools = load_tools()
#     tool_index = find_tool_index_by_id(tools, tool_id)

#     if tool_index == -1:
#         raise ValueError(f"No se encontró  la herramienta con ID {tool_id}")

#     # Validar tipo y estado si se proporcionan
#     if "tipo" in tool_data:
#         validate_tool_type(tool_data["tipo"])
#     if "estado" in tool_data:
#         validate_tool_status(tool_data["estado"])

#     # Actualizar campos
#     updated_tool = tools[tool_index].copy()
#     for key, value in tool_data.items():
#         # saltear el campo "id" ya que no se debe modificar
#         if key != "id":
#             updated_tool[key] = value

#     tools[tool_index] = updated_tool
#     save_tools(tools)
#     return updated_tool


# def delete_tool(tool_id: int) -> None:
#     """
#     Elimina la herramienta con el ID proporcionado.

#     La función elimina la herramienta del archivo JSON y actualiza la lista de
#     herramientas en memoria.

#     Args:
#         tool_id (int): ID de la herramienta a eliminar
#     Raises:
#         ValueError: Si no se encuentra la herramienta con el ID proporcionado
#     """
#     tools = load_tools()
#     tool_index = find_tool_index_by_id(tools, tool_id)
#     if tool_index == -1:
#         raise ValueError(f"No se encontró la herramienta con ID {tool_id}")
#     # Eliminar la herramienta del índice encontrado
#     tools.pop(tool_index)
#     # Guardar la lista de herramientas actualizada
#     save_tools(tools)
