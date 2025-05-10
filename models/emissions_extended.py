from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ExtendedEmission(BaseModel):
    name: Optional[str] = None
    originId: Optional[str] = None
    productName: Optional[str] = None
    description: Optional[str] = None
    organizationUnit: Optional[str] = None
    facility: Optional[str] = None
    provider: Optional[str] = None
    quantity: Optional[float] = None
    quantityUnit: Optional[str] = None
    cost: Optional[str] = None
    costUnit: Optional[str] = None
    emissonSource: Optional[str] = None
    emissonCategory: str
    emissonSubCategory: str
    CO2E: Optional [float] = None
    CO2E_unit: Optional[str] = None
    isRenewable: Optional[str] = None
    timestamp: datetime
    consumptionStartDate: Optional[datetime] = None
    consumptionEndDate: Optional[datetime] = None
    transactionStartDate: Optional[datetime] = None
    transactionEndDate: Optional[datetime] = None
    emissionFactor: Optional[str] = None
    emissionFactorLibrary: Optional[str] = None
    waterTransactionType: Optional[str] = None
    fuelType: Optional[str] = None
    dataQualityType: Optional[str] = None

class Metadata(BaseModel):
    createdAt: datetime
    name: str
    readCountRemaining: int
    timeToExpire: int

class ExtendedMSMWrapper(BaseModel):
    id: str
    metadata: Metadata
    record: List[ExtendedEmission]