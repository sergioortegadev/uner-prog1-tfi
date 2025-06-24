from typing import Dict, List, Any, Optional
from datetime import datetime
from model.model_data import load_json_file, save_json_file
from model.new_id import new_id
# from model.model_users import find_user_by_id
# from model.model_tools import find_tool_by_id, update_tool


FILE = "loans.json"
REQUIRED_LOAN_FIELDS = ["tool_id", "user_dni"]


def load_loans() -> List[Dict[str, Any]]:
 """Cargar préstamos desde el archivo JSON

 Regresa una lista de diccionarios de préstamos.
 """
 return load_json_file(FILE, [])


def save_loans(loans: List[Dict[str, Any]]) -> None:
 """Guardar préstamos en el archivo JSON

 Recibe una lista de diccionarios de préstamos y los guarda en el
 archivo JSON.
 """
 save_json_file(FILE, loans)

def create_loan(new_loan_data: Dict[str, Any], loans: List[Dict[str, Any]]) -> Dict[str, Any]:
 new_loan = {
    # "id": get_next_id(loans),
     "id": new_id(loans),
     "tool_id": new_loan_data["tool_id"],
     "user_dni": new_loan_data["user_dni"],
     "date_loan": datetime.now().isoformat(),
     "date_return": "",
     "state": "Pendiente",
     "observations": ""
 }

 loans.append(new_loan)
 save_loans(loans)
 loans_updated = load_loans()

 return {
  "message": "Asignación creada correctamente",
  "to_print": loans_updated[-1],
 }

# / / / / Reemplazada AQUI y en controller / / /
# def create_loan(loan_data: Dict[str, Any]) -> Dict[str, Any]:
#     """Crear nuevo préstamo"""
#     loans = load_loans()

#     # Validar campos requeridos
#     for field in REQUIRED_LOAN_FIELDS:
#         if field not in loan_data:
#             raise ValueError(f"El campo {field} es obligatorio")

#     # Validar que existan usuario y herramienta
#     user = find_user_by_id(loan_data["user_dni"])
#     if not user:
#         raise ValueError(
#             f"Usuario con DNI {loan_data['user_dni']} no encontrado")

#     tool = find_tool_by_id(loan_data["tool_id"])
#     if not tool:
#         raise ValueError(
#             f"Herramienta con ID {loan_data['tool_id']} no encontrada")

#     # Validar que la herramienta esté disponible
#     if tool["status"] != "Disponible":
#         raise ValueError(
#             f"La herramienta no está disponible (Estado: {tool['status']})")

#     # Crear préstamo
#     new_loan = {
#         "id": get_next_id(loans),
#         "tool_id": loan_data["tool_id"],
#         "user_dni": loan_data["user_dni"],
#         "date_loan": datetime.now().isoformat(),
#         "date_return": None,
#         "status": "Pendiente",
#         "observations": loan_data.get("observations", "")
#     }

#     # Actualizar estado de la herramienta
#     update_tool(tool["id"], {"estado": "En Uso"})

#     loans.append(new_loan)
#     save_loans(loans)
#     return new_loan

# # / / / / Reemplazada en controller / / /
# # def find_loan_index_by_id(loan_id: int, loans: List[Dict[str, Any]]) -> int:
#     """Buscar índice de préstamo por ID"""
#     for i, loan in enumerate(loans):
#         if loan["id"] == loan_id:
#             return i
#     return -1

# / / / / Reemplazada en controller / / /
# def return_loan(loan_id: int, return_data: Dict[str, Any]) -> Dict[str, Any]:
#     """Registrar devolución de préstamo.

#     Actualiza el registro del préstamo con la fecha de devolución y el estado,
#     y actualiza el estado de la herramienta a "Disponible".

#     Args:
#         loan_id (int): ID del préstamo a devolver.
#         return_data (Dict[str, Any]): Información de devolución, que puede incluir
#             'status' y 'observaciones'.

#     Returns:
#         Dict[str, Any]: El registro de préstamo actualizado.

#     Raises:
#         ValueError: Si el préstamo no se encuentra o ya ha sido devuelto.
#     """
#     loans = load_loans()
#     loan_index = find_loan_index_by_id(loan_id, loans)

#     # Verificar si el préstamo existe
#     if loan_index == -1:
#         raise ValueError(f"Préstamo con ID {loan_id} no encontrado")

#     # Verificar si el préstamo ya ha sido devuelto
#     if loans[loan_index].get("fecha_devolucion"):
#         raise ValueError("Este préstamo ya fue devuelto")

#     # Actualizar la fecha de devolución y el estado del préstamo
#     loans[loan_index]["fecha_devolucion"] = datetime.now().isoformat()
#     loans[loan_index]["estado"] = return_data.get("status", "Devuelto OK")

#     # Agregar observaciones si están presentes en return_data
#     if "observaciones" in return_data:
#         loans[loan_index]["observaciones"] = return_data["observaciones"]

#     # Cambiar el estado de la herramienta asociada a "Disponible"
#     update_tool(loans[loan_index].get("tool_id"), {"estado": "Disponible"})

#     # Guardar los cambios en el archivo de préstamos
#     save_loans(loans)

#     return loans[loan_index]

# / / / / Reemplazada en controller / / /
# def get_active_loans() -> List[Dict[str, Any]]:
#     """Obtener préstamos activos, es decir, aquellos que aún no han sido devueltos.

#     Regresa una lista de préstamos que no tienen fecha de devolución.
#     """
#     loans = load_loans()
#     return [loan for loan in loans if not loan.get("fecha_devolucion")]

# / / / / Reemplazada en controller / / /
# def get_user_loans(user_dni: int) -> List[Dict[str, Any]]:
#     """Obtener historial de préstamos de un usuario

#     Args:
#         user_dni (int): ID del usuario a buscar

#     Returns:
#         List[Dict[str, Any]]: Lista de préstamos del usuario
#     """
#     loans = load_loans()
#     return [loan for loan in loans if loan["user_dni"] == user_dni]

# / / / / Reemplazada en controller / / /
# def get_tool_loans(tool_id: int) -> List[Dict[str, Any]]:
#     """Obtener historial de préstamos de una herramienta

#     Args:
#         tool_id (int): ID de la herramienta a buscar

#     Returns:
#         List[Dict[str, Any]]: Lista de préstamos de la herramienta
#     """
#     # Cargar lista de préstamos
#     loans = load_loans()
#     # Filtrar préstamos por ID de herramienta
#     return [loan for loan in loans if loan["tool_id"] == tool_id]
