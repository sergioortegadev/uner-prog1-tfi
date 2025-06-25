import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.model_maintenance import load_maintenance

def maintenance_create(id_tool=None, date=None, maintenance_type=None, description=None, responsible=None, cost=None, next=None):
 if (not id_tool or not date or not maintenance_type or not description or not responsible or not cost or not next):
  return {
   'message': 'Error: Todos los campos son requeridos',
   'to_print': {}
  }
 if not isinstance(id_tool, int) or not isinstance(date, str) or not isinstance(maintenance_type, str) or not isinstance(description, str) or not isinstance(responsible, str) or not isinstance(cost, str) or not isinstance(next, str):
  return {
   'message': 'Error: El id_tool debe ser un entero, y los demás datos deben ser cadenas de texto.',
   'to_print': {}
  }
 # Simulación de creación de mantenimiento
 # Aquí se podría agregar la lógica para registrar la herramienta en una base de datos o sistema
 # Por ahora, simplemente retornamos un mensaje de éxito.
 return {
  'message': 'Mantenimiento Creado',
  'to_print': {   
    "id": 1,
    "id_tool": id_tool,
    "date": date,
    "maintenance_type": maintenance_type,
    "description": description,
    "responsible": responsible,
    "cost": cost,
    "next": next
  }
 }

def maintenance_list_all(*args, **kwargs):

 maintenance = load_maintenance()

 return {
    'message': 'Listado completo de mantenimientos' if maintenance else 'No hay mantenimientos registrados.',
    'to_print': maintenance if maintenance else []
 }


# Ejemplo de uso
# print(maintenance_create(2, '2025-5-16', 'Correctivo', 'Reparacion de carcaza', 'Estudiantes 5to año', '$350', 'N/A'))
# print(maintenance_create())
# print(maintenance_create('2', '2025-5-16', 'Correctivo', 'Reparacion de carcaza', 'Estudiantes 5to año', '$350', 'N/A'))
# print(maintenance_create(2))
# print(maintenance_list_all())
# print(maintenance_list_all('martillo'))