from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class EmissionData(BaseModel):
    product_id: str
    name: str
    product: str
    company: str
    source: str
    category: str
    sub_category: str
    CO2E: Optional[float] = None
    CO2E_unit: Optional[str] = None
    quantity: Optional[float] = None
    quantity_unit: Optional[str] = None
    timestamp: Optional[datetime] = None
    consumption_end_date: Optional[datetime] = None
    emission_factor: Optional[str] = None
    emission_factor_library: Optional[str] = None
    transaction_start_date: Optional[datetime] = None
    transaction_end_date: Optional[datetime] = None
    water_transaction_type: Optional[str] = None
    organizational_unit: Optional[str] = None
    facility: Optional[str] = None

class Metadata(BaseModel):
    createdAt: datetime
    name: str
    readCountRemaining: int
    timeToExpire: int

class MSMWrapper(BaseModel):
    id: str
    metadata: Metadata
    record: List[EmissionData]