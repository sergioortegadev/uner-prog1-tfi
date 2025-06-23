from typing import Dict, List, Any, Optional
from datetime import datetime
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.model_loans import load_loans, save_loans, create_loan
from controller.controller_tools import update_tool, tool_get_by_id
from controller.controller_users import user_get_by_dni

# Accesory funcions for loans
def find_loan_index_by_tool_id(tool_id: int, loans: List[Dict[str, Any]]) -> int:
    """Buscar índice de préstamo por ID de herramienta"""
    for i, loan in enumerate(loans):
        if loan["tool_id"] == tool_id and loan["state"] == "Pendiente":
            return i
    return -1

# Main functions for loans
def loan_list(*args, **kwargs) -> List[Dict[str, Any]]:
    return load_loans()

def loan_create(tool_id: int = None, user_dni: int = None) -> Dict[str, Any]:
 if not tool_id or not user_dni:
  return {
    'message': 'Error: ID de herramienta o DNI de usuario no proporcionados. \n Esta función requiere ambos parámetros.',
    'to_print': {}
  }
 if not isinstance(tool_id, int) or not isinstance(user_dni, int):
  return {
   'message': 'Error: El ID de herramienta y el DNI del usuario deben ser números enteros',
   'to_print': {}
  }

 loans = load_loans()

 # Validar que existan usuario y herramienta
 user = user_get_by_dni(user_dni).get('to_print', None)
 if not user:
  return {
     'message': f'Error: No se encontró un usuario con el DNI {user_dni}.',
     'to_print': {}
    }

 # Verificar si la herramienta existe
 tool = tool_get_by_id(tool_id).get('to_print', None)
 if not tool:
  return {
     'message': f'Error: No se encontró una herramienta con el ID {tool_id}.',
     'to_print': {}
    }

 # Verificar que la herramienta esté disponible
 if tool.get('tool_available') is False:
  return {
   'message': f'Error: La herramienta con ID {tool_id} no está disponible.',
   'to_print': {}
  }

 # Actualizar el estado de la herramienta
 update_tool(tool_id, {"tool_available": False})

 # Crear nuevo préstamo
 new_loan_data = {
  'tool_id': tool_id,
  'user_dni': user_dni
 }

 return create_loan(new_loan_data, loans)

def loan_return(tool_id: int = None, observation: str = None) -> Dict[str, Any]:
 if not tool_id:
  return {
    'message': 'Error: ID de herramienta no proporcionados. \n Esta función requiere ese parámetro.',
    'to_print': {}
  }
 if not isinstance(tool_id, int):
  return {
   'message': 'Error: El ID de herramienta debe ser un número entero',
   'to_print': {}
  }

 loans = load_loans()
 loan_index = find_loan_index_by_tool_id(tool_id, loans)

 # Verificar si el préstamo existe
 if loan_index == -1:
  return {
   'message': f'Error: No se encontró un préstamo para la herramienta con ID {tool_id}.',
   'to_print': {}
  }
 
 # Verificar si el préstamo ya ha sido devuelto
 if loans[loan_index].get("fecha_devolucion"):
  return {
   'message': f'Error: La herramienta con ID {tool_id} ya ha sido devuelta. O no se encuentra en estado "Pendiente".',
   'to_print': {}
  }

 # = = = Procede a registrar la devolución = = =
 # Actualizar la fecha de devolución y el estado del préstamo
 loans[loan_index]["date_return"] = datetime.now().isoformat()
 loans[loan_index]["state"] = "Devuelto"

 # Si se proporciona una observación, agregarla al préstamo
 if observation:
  loans[loan_index]["observation"] = observation

 # Actualizar el estado de la herramienta a "Disponible"
 update_tool(tool_id, {"tool_available": True})

 # Guardar los cambios en el archivo de préstamos
 save_loans(loans)


 return {
  'message': 'Devolución Realizada',
  'to_print': loans[loan_index]
 }

def loan_get_tools_pending_return(*args, **kwargs) -> List[Dict[str, Any]]:
    loans = load_loans()
    loans_tools_pending_return = []
    for loan in loans:
        if loan['state'] == 'Pendiente':
            loans_tools_pending_return.append(loan)

    return loans_tools_pending_return if len(loans_tools_pending_return) > 0 else {
        'message': f'No se encontraron herramientas pendientes de devolución.',
        'to_print': {}
    }

def loan_get_tool(tool_id: int = None)-> List[Dict[str, Any]]:
    if not tool_id:
        return {
            'message': 'Error: ID de herramienta no proporcionado.\n Esta función requiere un ID de herramienta.',
            'to_print': {}
        }
    if not isinstance(tool_id, int):
        return {
            'message': 'Error: El ID de herramienta debe ser un número entero',
            'to_print': {}
        }
    
    loans = load_loans()
    loans_tools_by_id = []
    for loan in loans:
        if loan['tool_id'] == tool_id:
            loans_tools_by_id.append(loan)

    return {
       'message': 'Historial de la herramienta' if len(loans_tools_by_id) > 0 else f'No hay historial de préstamos para la herramienta con Id {tool_id}.',
       'to_print': loans_tools_by_id if len(loans_tools_by_id) > 0 else []
    }

def loan_get_user(user_dni: int = None) -> List[Dict[str, Any]]:
    if not user_dni or user_dni is None:
        return {
            'message': f'Error: DNI de usuario no proporcionado. Esta función requiere un DNI de usuario.',
            'to_print': {}
        }
    if not isinstance(user_dni, int):
        return {
            'message': 'Error: El DNI del usuario debe ser un número entero',
            'to_print': {}
        }
    
    loans = load_loans()
    loans_user_by_dni = []
    for loan in loans:
        if loan['user_dni'] == user_dni:
            loans_user_by_dni.append(loan)
    return {
        'message': 'Historial del usuario' if len(loans_user_by_dni) > 0 else f'No hay historial de préstamos para usuario con DNI {user_dni}.',
        'to_print': loans_user_by_dni if len(loans_user_by_dni) > 0 else []
    }


# Ejemplos de uso
# print(loan_create(28, 99667744))
# print(loan_create())
# print(loan_create('',''))
# print(loan_return(30, 'Muy desgastada'))
# print(loan_return(1, 'Roto al devolverlo'))
# print(loan_return())
# print(loan_list())
# print(loan_get_tool(4))
# print(loan_get_tool(14))
# print(loan_get_tool())
# print(loan_get_tool(''))
# print(loan_get_tool('abc'))
# print(loan_get_tools_pending_return())
# print(loan_get_user(11223344))
# print(loan_get_user())
# print(loan_get_user(''))
# print(loan_get_user('abc' ))