import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_path = os.path.join(BASE_DIR, "data", "tools.json")

def tools():
    print('Cargando herramientas...')
    with open(json_path, 'r', encoding='utf-8') as f:
        tools_data = json.load(f)
    return tools_data

