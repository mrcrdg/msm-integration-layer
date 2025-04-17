from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
import json
import uuid

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
    organizational_unit: Optional[str] = None

# New models:
class Metadata(BaseModel):
    createdAt: datetime
    name: str
    readCountRemaining: int
    timeToExpire: int

class MSMWrapper(BaseModel):
    id: str
    metadata: Metadata
    record: List[EmissionData]

# Load full wrapped payload from file
with open("data/data.json") as f:
    raw_data  = json.load(f)

# Convert the inner record to validated model list
emission_data = [EmissionData(**item) for item in raw_data]

# Build the final validated MSM payload
msm_payload = MSMWrapper(
    id=uuid.uuid4().hex[:24],
    metadata=Metadata(
        createdAt=datetime.utcnow(),
        name="SUSTAINABILITY",
        readCountRemaining=77,
        timeToExpire=86400
    ),
    record=emission_data
)

# Route returning the wrapped MSM payload
@app.get("/emissions", response_model=MSMWrapper)
def get_msm_payload():
    return msm_payload
    
