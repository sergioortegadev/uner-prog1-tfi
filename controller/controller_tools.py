import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def tool_get_by_id(id=None):
 if not id:
  return {
    'message': 'Error: ID de herramienta no proporcionado. \n Esta función requiere el parámetro ID.',
    'to_print': {}
  }
 if not isinstance(id, int):
  return {
   'message': 'Error: El ID de la herramienta debe ser un número entero',
   'to_print': {}
  }
 # Simulación de obtención de herramienta por ID
 # Aquí se podría agregar la lógica para obtener la herramienta de una base de datos o sistema
 return {
  'message': 'Datos de la Herramienta ',
  'to_print': { 
   "tool_id": 1,
   "tool_name": "martillo",
   "tool_type": "algo",
   "tool_brand": "Truper",
   "tool_model": "MX123",
   "tool_state": "nuevo",
   "tool_location": "S01-E01-R01",
   "tool_observations": "",
   "tool_available": True
  },
 }

def tool_get_by_name(name=None):
 if not name:
  return {
    'message': 'Error: Nombre de herramienta no proporcionado. \n Esta función requiere el parámetro "name".',
    'to_print': {}
  }
 if not isinstance(name, str):
  return {
   'message': 'Error: El nombre de la herramienta debe ser una cadena de texto',
   'to_print': {}
  }
 # Simulación de obtención de herramienta por nombre
 # Aquí se podría agregar la lógica para obtener la herramienta de una base de datos o sistema
 return {
  'message': 'Datos de la Herramienta ',
  'to_print': { 
   "tool_id": 1,
   "tool_name": "martillo",
   "tool_type": "algo",
   "tool_brand": "Truper",
   "tool_model": "MX123",
   "tool_state": "nuevo",
   "tool_location": "S01-E01-R01",
   "tool_observations": "",
   "tool_available": True
  },
 }

def tools_list_all(*args, **kwargs):
 # Estos parámetros, permite que acepte argumentos opcionales y los ignore. Sin ellos se rompe la ejecución si se le pasa un argumento que no espera.

 # Simulación de listado de herramientas
 # Aquí se podría agregar la lógica para obtener las herramientas de una base de datos o sistema
 # Por ahora, simplemente retornamos un mensaje de éxito con datos simulados

 return {
  'message': 'Listado de Herramientas',
  'to_print': [
  { 
   "tool_id": 1,
   "tool_name": "martillo",
   "tool_type": "algo",
   "tool_brand": "Truper",
   "tool_model": "MX123",
   "tool_state": "nuevo",
   "tool_location": "S01-E01-R01",
   "tool_observations": "",
   "tool_available": True
  },
  {
    "tool_id": 2,
    "tool_name": "Destornillador plano",
    "tool_type": "algo",
    "tool_brand": "Stanley",
    "tool_model": "DX123",
    "tool_state": "usado",
    "tool_location": "S01-E01-R02",
    "tool_observations": "",
    "tool_available": False
  },
  {
    "tool_id": 3,
    "tool_name": "Destornillador Phillips",
    "tool_type": "algo",
    "tool_brand": "Stanley",
    "tool_model": "DX124",
    "tool_state": "usado",
    "tool_location": "S01-E01-R03",
    "tool_observations": "",
    "tool_available": True
  },
  { 
   "tool_id": 4,
   "tool_name": "Llave inglesa",
   "tool_type": "algo",
   "tool_brand": "Bahco",
   "tool_model": "LX123",
   "tool_state": "nuevo",
   "tool_location": "S01-E01-R04",
   "tool_observations": "",
   "tool_available": True
  }
  ]
 }

def tools_list_by_type(tool_type=None):
 if not tool_type:
  return {
   'message': 'Error: Tipo de herramienta no proporcionado. \n Esta función requiere el parámetro tool_type.',
   'to_print': {}
  }
 if not isinstance(tool_type, str):
  return {
   'message': 'Error: El tipo de herramienta debe ser una cadena de texto.',
   'to_print': {}
  }
 # Simulación de listado de herramientas por tipo
 # Aquí se podría agregar la lógica para obtener las herramientas de una base de datos o sistema
 return {
  'message': 'Listado de Herramientas por Tipo',
  'to_print': [
   {
    "tool_id": 1,
    "tool_name": "martillo",
    "tool_type": tool_type,
    "tool_brand": "Truper",
    "tool_model": "MX123",
    "tool_state": "nuevo",
    "tool_location": "S01-E01-R01",
    "tool_observations": "",
    "tool_available": True
   },
   {
    "tool_id": 5,
    "tool_name": "martillo grande",
    "tool_type": tool_type,
    "tool_brand": "Stanley",
    "tool_model": "DX123",
    "tool_state": "usado",
    "tool_location": "S01-E01-R02",
    "tool_observations": "muy desgastado",
    "tool_available": False
   },
   {
    "tool_id": 13,
    "tool_name": "martillo para chapa",
    "tool_type": tool_type,
    "tool_brand": "Stanley",
    "tool_model": "DX124",
    "tool_state": "usado",
    "tool_location": "S01-E01-R03",
    "tool_observations": "",
    "tool_available": True
   }
  ]
 }

def tool_create(name=None, tool_type=None, brand=None, model=None, state=None, location=None, observations=None, available=None):
 if not name or not tool_type or not brand or not model or not state or not location or available == None:
  return {
   'message': 'Error: Todos los campos son requeridos, menos observaciones.',
   'to_print': {}
  }
 if not isinstance(name, str) or not isinstance(tool_type, str) or not isinstance(brand, str) or not isinstance(model, str) or not isinstance(state, str) or not isinstance(location, str) or not isinstance(observations, str):
  return {
   'message': 'Error: El nombre, el tipo, la marca, el modelo, el estado, la ubicación y/o las observaciones de la herramienta deben ser cadenas de texto.',
   'to_print': {}
  }
 if not isinstance(available, bool):
  return {
   'message': 'Error: La disponibilidad de la herramienta debe ser un valor booleano (True o False).',
   'to_print': {}
  }
 # Simulación de creación de herramienta
 # Aquí se podría agregar la lógica para registrar la herramienta en una base de datos o sistema
 # Por ahora, simplemente retornamos un mensaje de éxito
 return {
  'message': 'Herramienta Creada',
  'to_print': {
   "tool_id": 1,
   "tool_name": name,
   "tool_type": tool_type,
   "tool_brand": brand,
   "tool_model": model,
   "tool_state": state,
   "tool_location": location,
   "tool_observations": observations,
   "tool_available": available
  }
 }

def tool_update(id=None):
 if not id:
  return {
   'message': 'Error: ID de herramienta no proporcionado. \n Esta función requiere el parámetro ID.',
   'to_print': {}
  }
 if not isinstance(id, int):
  return {
   'message': 'Error: El ID de la herramienta debe ser un número entero',
   'to_print': {}
  }
 # Simulación de actualización de herramienta
 # Aquí se podría agregar la lógica para actualizar la herramienta en una base de datos o sistema
 # Por ahora, simplemente retornamos un mensaje de éxito
 return {
  'message': 'Herramienta Actualizada',
  'to_print': { 
   "tool_id": 1,
   "tool_name": "martillo",
   "tool_type": "algo",
   "tool_brand": "Truper",
   "tool_model": "MX123",
   "tool_state": "nuevo",
   "tool_location": "S01-E01-R01",
   "tool_observations": "rota",
   "tool_available": False
  }
 }

def tool_delete(id=None):
 if not id:
  return {
    'message': 'Error: ID de herramienta no proporcionado. \n Esta función requiere el parámetro ID.',
    'to_print': {}
  }
 if not isinstance(id, int):
  return {
   'message': 'Error: El ID de la herramienta debe ser un número entero',
   'to_print': {}
  }
 # Simulación de eliminación de herramienta 
 # Aquí se podría agregar la lógica para eliminar el usuario en una base de datos o sistema
 # Por ahora, simplemente retornamos un mensaje de éxito
 return {
  'message': 'Herramienta Eliminada',
  'to_print': { 
   "tool_id": 1,
   "tool_name": "martillo",
   "tool_type": "algo",
   "tool_brand": "Truper",
   "tool_model": "MX123",
   "tool_state": "nuevo",
   "tool_location": "S01-E01-R01",
   "tool_observations": "rota",
   "tool_available": False
  }
 }




# Ejemplo de uso
# print(tool_get_by_id(1))
# print(tool_get_by_name('martillo'))
# print(tool_get_by_name(''))
# print(tool_get_by_name())
# print(tool_create("Martillo", "Truper", "nuevo", False))
# print(tool_create("Martillo", "Truper", 1, False))
# print(tool_create("Martillo", "Truper", "usado", ''))
# print(tool_create())
# print(tool_create("Martillo", "Truper", "nuevo"))
# print(tools_list_all())
# print(tools_list_all('martillo'))
# print(tools_list_by_type('martillo'))
# print(tools_list_by_type(''))
# print(tools_list_by_type())
# print(tool_update(2))
# print(tool_update('2'))
# print(tool_update())
# print(tool_delete(2))
# print(tool_delete('2'))
# print(tool_delete())