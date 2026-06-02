from app.services.parsers.kaufland_parser import parse_kaufland
from app.services.ocr_normalizer import normalize_text
from app.services.ocr import ocr_image
from app.services.postprocessor.db_name_matcher import match_product
from app.db.session import SessionLocal
from app.services.postprocessor.quantity import add_quantity

from datetime import datetime
import uuid

async def run_pipeline(image_input):

    raw_text = ocr_image(image_input)
    cleaned_text = normalize_text(raw_text)

    result = parse_kaufland(cleaned_text)

    result["date"] = datetime.now().strftime("%b %d %H:%M")

    async with SessionLocal() as db:

        for item in result["items"]:
            matched = await match_product(db, item["name"])

            item["category"] = matched["category"]
            item["name"] = matched["name"]
    
    result["items"] = add_quantity(result["items"])

    return result