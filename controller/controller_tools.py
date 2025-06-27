from typing import Dict, List, Any, Optional
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.model_tools import load_tools, save_tools, create_tool

tools = load_tools()

def update_tool(tool_id: int, updates: dict) -> dict:

 for t in tools:
  if t['id'] == tool_id:
   t['disponible'] = updates.get('disponible', t['disponible'])
   break

 save_tools(tools)

def tool_get_by_id(id_tool: int = None) -> Dict[str, Any]:
 if not id_tool:
  return {
    'message': 'Error: ID de herramienta no proporcionado. \n Esta función requiere el parámetro ID.',
    'to_print': {}
  }
 if not isinstance(id_tool, int):
  return {
   'message': 'Error: El ID de la herramienta debe ser un número entero',
   'to_print': {}
  }
 
 tools = load_tools()
 tool = None
 for t in tools:
  if t['id'] == id_tool:
   tool = t
   break


 return {
  'message': 'Datos de la Herramienta' if tool else 'Herramienta no encontrada',
  'to_print': tool if tool else {}
 }

def tool_get_by_name(partial_name=None):
 if not partial_name:
  return {
    'message': 'Error: Nombre de herramienta no proporcionado. Esta función requiere el parámetro "name".',
    'to_print': {}
  }
 if not isinstance(partial_name, str):
  return {
   'message': 'Error: El nombre de la herramienta debe ser una cadena de texto',
   'to_print': {}
  }
 
 matches = [
        tool for tool in tools
        if 'nombre' in tool and partial_name.lower() in tool['nombre'].lower()
 ]

 if not matches:
        return {
            'message': 'La herramienta con el nombre proporcionado no existe.',
            'to_print': {}
        }

 return {
        'message': f'Se encontraron {len(matches)} coincidencia(s).',
        'to_print': matches
 }


def tools_list_all(*args, **kwargs) -> List[Dict[str, Any]]:

 tools = load_tools()

 return {
  'message': 'Listado de Herramientas' if len(tools) > 0 else 'No hay herramientas registradas',
  'to_print': tools if len(tools) > 0 else []
 }


def tool_create(nombre: str = None, tipo: str = None, marca: str = None, modelo: str = None, estado: str = None, ubicacion: str = None, observaciones: str = ''):
 if not nombre or not tipo or not marca or not modelo or not estado or not ubicacion:
  return {
   'message': 'Error: Todos los campos son requeridos, menos observaciones.',
   'to_print': {}
  }
 if not isinstance(nombre, str) or not isinstance(tipo, str) or not isinstance(marca, str) or not isinstance(modelo, str) or not isinstance(estado, str) or not isinstance(ubicacion, str) or not isinstance(observaciones, str):
  return {
   'message': 'Error: El nombre, el tipo, la marca, el modelo, el estado, la ubicación y/o las observaciones de la herramienta deben ser cadenas de texto.',
   'to_print': {}
  }

 new_tool = {
        "nombre": nombre,
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "estado": estado,
        "ubicacion": ubicacion,
        "observaciones": observaciones
    }

 created_tool = create_tool(new_tool)

 return {
  'message': 'Herramienta Creada' if created_tool else 'Error al crear la herramienta',
  'to_print': created_tool if created_tool else {}
 }

def tool_update(tool_id: Optional[int],datos_herramienta: Optional[Dict[str, Any]] = None, nombre: str = None, tipo: str = None, marca: str = None, modelo: str = None, estado: str = None, ubicacion: str = None, observaciones: str = ''):
 if not tool_id:
  return {
   'message': 'Error: ID de herramienta no proporcionado. \n Esta función requiere el parámetro ID.',
   'to_print': {}
  }
 if not isinstance(tool_id, int):
  return {
   'message': 'Error: El ID de la herramienta debe ser un número entero',
   'to_print': {}
  }
 
 tool = tool_get_by_id(tool_id)['to_print']
 if tool is None:
  return {
            'message': 'Error: La herramiento con el ID proporcionado no existe.',
            'to_print': {}
        }
 
 data_new = {
  "nombre":  nombre,
  "tipo": tipo,
  "marca": marca,
  "modelo":modelo,
  "estado": estado,
  "ubicacion": ubicacion,
  "observaciones":  observaciones,
 }

 for t in tools:
  if t['id'] == tool_id:
   t['nombre'] = data_new.get('nombre', t['nombre'])
   t['tipo'] = data_new.get('tipo', t['tipo'])
   t['marca'] = data_new.get('marca', t['marca'])
   t['modelo'] = data_new.get('modelo', t['modelo'])
   t['estado'] = data_new.get('estado', t['estado'])
   t['ubicacion'] = data_new.get('ubicacion', t['ubicacion'])
   t['observaciones'] = data_new.get('observaciones', t['observaciones'])
   break

 save_tools(tools)

 return {
     'message': 'Herramienta actualizada en estos campos',
     'to_print': data_new
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
 
 tools = load_tools()
 tool_to_delete = None
 for t in tools:
  if t['id'] == id:
   tool_to_delete = t
   break

 if not tool_to_delete:
  return {
   'message': 'Herramienta no encontrada',
   'to_print': {}
  }
 confirmation = input(f"¿Estás seguro de que deseas eliminar la herramienta con ID {id}? (s/n): ")
 if confirmation.lower() != 's':
  return {
   'message': 'Eliminación cancelada',
   'to_print': {}
  }

 tools = [t for t in tools if t['id'] != id]
 save_tools(tools)

 return {
  'message': 'Herramienta eliminada correctamente',
  'to_print': tool_to_delete
 }
