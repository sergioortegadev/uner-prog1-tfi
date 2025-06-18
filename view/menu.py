import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import controller.controller_tools

def menu():
   option = input('' \
   '\n\n  - - Menú Principal - - ' \
   
   '\n\n Seleccione una opción: \n ' \
   '1. Probar funcion tools \n ' \
   '0. Salir \n Opción: ')

   match option:
       case '1':
           tool_loan()
           menu()
       case '0':
           print('Saliendo de la aplicación...')
           sys.exit()
       case _:
           print('Opción no válida. Intente de nuevo.')
           menu()


def tool_loan():
    loan = input(' Ingrese el ID de la herramienta: ')
    tool_id = int(loan)
    user_dni = input(' Ingrese el DNI del usuario: ')
    controller.controller_tools.tools_loan(tool_id, user_dni)
    menu()



