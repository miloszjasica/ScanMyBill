from fastapi import FastAPI
from app.db.base import Base
from app.models.receipt import Receipt
from app.db.session import engine
from app.api.receipts import router as receipts_router
from app.api.categories import router as categories_router

app = FastAPI(title="ScanMyBill API")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
def root():
    return {"message": "ScanMyBill API running"}

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(receipts_router, prefix="/receipts")
app.include_router(categories_router, prefix="/categories")