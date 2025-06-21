import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
 # Estos parámetros, permite que acepte argumentos opcionales y los ignore. Sin ellos se rompe la ejecución si se le pasa un argumento que no espera.
 
 # Simulación de listar el historial completo de mantenimientos
 # Aquí se podría agregar la lógica para obtener el historial completo de una base de datos o sistema
 # Por ahora, simplemente retornamos un mensaje de éxito con datos simulados
 return {
  'message': 'Historial de Mantenimiento',
  'to_print': [
   {
  "id": 1,
  "id_tool": 1,
  "date": "2025-06-03",
  "maintenance_type": "Correctivo",
  "description": "Cambio de escobillas",
  "responsible": "Estudiantes de 7mo año",
  "cost": "$0",
  "next": "N/A"
 },
 {
  "id": 2,
  "id_tool": 2,
  "date": "2025-05-20",
  "maintenance_type": "Preventivo",
  "description": "Lubricación de engranajes",
  "responsible": "Profesor Martínez",
  "cost": "$1500",
  "next": "2025-11-20"
 },
 {
  "id": 3,
  "id_tool": 3,
  "date": "2025-04-15",
  "maintenance_type": "Correctivo",
  "description": "Reemplazo de cable de alimentación",
  "responsible": "Estudiantes de 6to año",
  "cost": "$500",
  "next": "N/A"
 },
 {
  "id": 4,
  "id_tool": 4,
  "date": "2025-03-10",
  "maintenance_type": "Preventivo",
  "description": "Inspección general y limpieza",
  "responsible": "Profesor Gómez",
  "cost": "$0",
  "next": "2025-09-10"
 }
  ]
 }


# Ejemplo de uso
# print(maintenance_create(2, '2025-5-16', 'Correctivo', 'Reparacion de carcaza', 'Estudiantes 5to año', '$350', 'N/A'))
# print(maintenance_create())
# print(maintenance_create('2', '2025-5-16', 'Correctivo', 'Reparacion de carcaza', 'Estudiantes 5to año', '$350', 'N/A'))
# print(maintenance_create(2))
# print(maintenance_list_all())
# print(maintenance_list_all('martillo'))