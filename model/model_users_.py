import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_path = os.path.join(BASE_DIR, "data", "users.json")

def users():
 with open(json_path, 'r', encoding='utf-8') as f:
     users_data = json.load(f)
 return users_data