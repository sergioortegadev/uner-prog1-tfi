import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def loan_create(tool_id=None, user_dni=None):
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
 # Simulación de préstamo de herramienta
 # Aquí se podría agregar la lógica para registrar el préstamo en una base de datos o sistema
 # Por ahora, simplemente retornamos un mensaje de éxito
 return {
  'message': 'Prestamo Realizado',
  'to_print': {
   'Herramienta': tool_id,
   'Asignada a': user_dni
  }
 }

def loan_return(tool_id=None, user_dni=None, observation=None):
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
 # Simulación de devolución de herramienta
 # Aquí se podría agregar la lógica para registrar la devolución en una base de datos o sistema
 # Por ahora, simplemente retornamos un mensaje de éxito
 return {
  'message': 'Devolución Realizada',
  'to_print': {
   'Herramienta': tool_id,
   'Devuelta por': user_dni,
   'Observación': observation if observation else 'Ninguna'
  }
 }

def loan_list():
    # Simulación de listado de préstamos
    # Aquí se podría agregar la lógica para obtener los préstamos de una base de datos o sistema
    # Por ahora, simplemente retornamos un mensaje de éxito con datos simulados
    return {
        'message': 'Listado de Préstamos',
        'to_print': [
            {'Herramienta': 1, 'Asignada a': 12345678, 'Estado': 'Prestada'},
            {'Herramienta': 2, 'Asignada a': 87654321, 'Estado': 'Devuelta'},
            {'Herramienta': 3, 'Asignada a': 11223344, 'Estado': 'Prestada'}
        ]
    }

def loan_get_tool(tool_id=None):
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
    # Simulación de obtención de herramienta por ID
    # Aquí se podría agregar la lógica para obtener la herramienta de una base de datos o sistema
    return {
        'message': 'Historial de la herramienta',
        'to_print': [
            {'Herramienta': tool_id, 'Asignada a': 12345678, 'Estado': 'Prestada'},
            {'Herramienta': tool_id, 'Asignada a': 87654321, 'Estado': 'Devuelta'},
            {'Herramienta': tool_id, 'Asignada a': 11223344, 'Estado': 'Prestada'}
        ]
    }

def loan_get_user(user_dni=None):
    if not user_dni or user_dni is None:
        return {
            'message': 'Error: DNI de usuario no proporcionado.\n Esta función requiere un DNI de usuario.',
            'to_print': {}
        }
    if not isinstance(user_dni, int):
        return {
            'message': 'Error: El DNI del usuario debe ser un número entero',
            'to_print': {}
        }
    # Simulación de obtención de préstamos por DNI de usuario
    # Aquí se podría agregar la lógica para obtener los préstamos de una base de datos o sistema
    return {
        'message': 'Historial del usuario',
        'to_print': [
            {'Herramienta': 1, 'Asignada a': user_dni, 'Estado': 'Prestada'},
            {'Herramienta': 2, 'Asignada a': user_dni, 'Estado': 'Devuelta'},
            {'Herramienta': 3, 'Asignada a': user_dni, 'Estado': 'Prestada'}
        ]
    }


# Ejemplos de uso
# print(loan_create(1, 12345678))
# print(loan_create())
# print(loan_create('',''))
# print(loan_return(1, 12345678))
# print(loan_return())
# print(loan_return(1, 12345678, 'Roto al devolverlo'))
# print(loan_list())
# print(loan_get_tool(1))
# print(loan_get_tool())
# print(loan_get_tool(''))
# print(loan_get_tool('abc'))
# print(loan_get_user(12345678))
# print(loan_get_user())
# print(loan_get_user(''))
# print(loan_get_user('abc' ))