from fastapi import APIRouter
from models.emissions_extended import Metadata, ExtendedMSMWrapper, ExtendedEmission
from datetime import datetime
import uuid
import json

router = APIRouter()

with open("data/extended_data.json", "r") as f:
    extended_data = json.load(f)

# Validate using Pydantic (ensures types are correct)
extended_records = [ExtendedEmission(**item) for item in extended_data]

@router.get("/extended", response_model=ExtendedMSMWrapper)
def get_extended_payload():
    return ExtendedMSMWrapper(
        id=uuid.uuid4().hex[:24],
        metadata=Metadata(
            createdAt=datetime.utcnow(),
            name="Sustainability data",
            readCountRemaining=77,
            timeToExpire=86400
        ),
        record=extended_records
    )