from typing import Dict, Any, Optional
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.model_maintenance import load_maintenance, create_maintenance
from controller.controller_tools import tool_get_by_id
from controller.controller_tools import update_tool

maintenance = load_maintenance()

def maintenance_create(tool_id: Optional[int], maintenance_data: Optional[Dict[str, Any]] = None, fecha: str = None, tipo: str = None, descripcion: str = None, responsable: str = None, costo: str = None, siguiente: str = None):
 if (not tool_id):
  return {
   'message': 'Error: Todos los campos son requeridos',
   'to_print': {}
  }
 
 tool = tool_get_by_id(tool_id)['to_print']
 if not tool:
  return {
   'message': 'Error: Herramienta no encontrada con ese ID',
   'to_print': {}
  }
 
 new_data = {
  "tool_id": tool_id,
  "herramienta": tool['nombre'],
  "fecha": fecha,
  "tipo": tipo,
  "descripcion": descripcion,
  "responsable": responsable,
  "costo": costo,
  "siguiente": siguiente, 
 }

 created_maintenance = create_maintenance(new_data)

 return {
  'message': 'Registro de mantenimiento realizado con éxito' if created_maintenance else 'No se pudo registrar el mantenimiento.',
    'to_print': created_maintenance if created_maintenance else []
 }
 

def maintenance_list_all(*args, **kwargs):

 maintenance = load_maintenance()

 return {
    'message': 'Listado completo de mantenimientos' if maintenance else 'No hay mantenimientos registrados.',
    'to_print': maintenance if maintenance else []
 }