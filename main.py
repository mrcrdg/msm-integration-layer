from fastapi import FastAPI
from routes.emissions import router as raw_router
from routes.emissions_extended import router as extended_router

app = FastAPI()

app.include_router(raw_router, prefix="/emissions")
app.include_router(extended_router, prefix="/emissions")