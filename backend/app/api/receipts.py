from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel

from app.db.session import SessionLocal
from app.models.receipt import Receipt
from app.services.pipeline import run_pipeline

router = APIRouter()


class ScanRequest(BaseModel):
    receipt_id: str | None = None
    raw_text: str


@router.post("/scan")
async def scan_receipt(file: UploadFile = File(...)):
    image_bytes = await file.read()

    result = await run_pipeline(image_bytes)

    return {
        "receipt_id": None,
        "data": result
    }


class ConfirmReceipt(BaseModel):
    receipt_id: str
    merchant: str | None
    total: float | None
    raw_text: str | None


@router.post("/confirm")
async def confirm_receipt(data: ConfirmReceipt):
    async with SessionLocal() as db:

        receipt = Receipt(
            id=data.receipt_id,
            merchant=data.merchant,
            total=data.total,
            raw_text=data.raw_text
        )

        db.add(receipt)
        await db.commit()

    return {"status": "saved"}