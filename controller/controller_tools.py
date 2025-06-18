import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import model.model_tools
import model.model_users

def tools_loan(tool_id, user_dni):
 tools = model.model_tools.tools()
 users = model.model_users.users()
 new_loan = {
     'tool_id': "",
     'user_dni': ""
 }
 for tool in tools:
     if tool.get('tool_id') == tool_id:

         new_loan['tool_id'] = tool.get('tool_id')
         break
     
 for user in users:
     if user.get('user_dni') == user_dni:

         new_loan['user_dni'] = user.get('user_dni')
         break

 print('\nPrestamo Realizado: \nHerramienta: ', new_loan['tool_id'], 'Asignada a : ', new_loan['user_dni'], '\n', new_loan)
