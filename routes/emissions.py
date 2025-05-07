from fastapi import APIRouter
from models.emissions import EmissionData, Metadata, MSMWrapper
from datetime import datetime
import uuid
import json

router = APIRouter()

with open("data/data.json", "r") as f:
    raw_data = json.load(f)

emission_data = [EmissionData(**item) for item in raw_data]

@router.get("", response_model=MSMWrapper)
def get_msm_payload():
    return MSMWrapper(
        id=uuid.uuid4().hex[:24],
        metadata=Metadata(
            createdAt=datetime.utcnow(),
            name="Sustainability data",
            readCountRemaining=77,
            timeToExpire=86400
        ),
        record=emission_data
    )