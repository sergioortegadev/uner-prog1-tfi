from typing import Dict, List, Any, Optional
from datetime import datetime
from model.model_data import load_json_file, save_json_file
from model.new_id import new_id

FILE = "loans.json"
REQUIRED_LOAN_FIELDS = ["tool_id", "user_dni"]


def load_loans() -> List[Dict[str, Any]]:
 return load_json_file(FILE, [])


def save_loans(loans: List[Dict[str, Any]]) -> None:
 save_json_file(FILE, loans)

def create_loan(new_loan_data: Dict[str, Any], loans: List[Dict[str, Any]]) -> Dict[str, Any]:
 new_loan = {
     "id": new_id(loans),
     "tool_id": new_loan_data["tool_id"],
     "user_dni": new_loan_data["user_dni"],
     "date_loan": datetime.now().isoformat(),
     "date_return": "",
     "state": "Pendiente",
     "observations": ""
 }

 loans.append(new_loan)
 save_loans(loans)
 loans_updated = load_loans()

 return {
  "message": "Asignación creada correctamente",
  "to_print": loans_updated[-1],
 }
