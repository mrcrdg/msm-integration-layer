# main.py
from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
import json

app = FastAPI()

# Define the structure of one emission record
class EmissionData(BaseModel):
    product_id: str
    name: str
    category: str
    sub_category: str
    company: str
    CO2E: Optional[float] = None
    CO2E_unit: Optional[str] = None
    quantity: Optional[float] = None
    quantity_unit: Optional[str] = None
    timestamp: Optional[datetime] = None
    consumption_end_date: Optional[datetime] = None
    emission_factor: Optional[str] = None
    emission_factor_library: Optional[str] = None
    facility: Optional[str] = None
    transaction_start_date: Optional[datetime] = None
    transaction_end_date: Optional[datetime] = None
    unit: Optional[str] = None
    water_transaction_type: Optional[str] = None

# Load data from external JSON file
with open("data/data.json") as f:
    raw_data = json.load(f)
    data = [EmissionData(**item) for item in raw_data]

@app.get("/emissions", response_model=List[EmissionData])
def get_emissions():
    return data
