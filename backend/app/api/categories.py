from fastapi import APIRouter
from pydantic import BaseModel

from app.db.session import SessionLocal
from app.models.category import Category
from app.models.category_keyword import CategoryKeyword

router = APIRouter()


class CategoryCreate(BaseModel):
    name: str


@router.post("/")
async def create_category(data: CategoryCreate):
    async with SessionLocal() as db:

        category = Category(name=data.name)
        db.add(category)
        await db.commit()
        await db.refresh(category)

        return category
    

    
class KeywordCreate(BaseModel):
    category_id: int
    keyword: str


@router.post("/keyword")
async def add_keyword(data: KeywordCreate):
    async with SessionLocal() as db:

        kw = CategoryKeyword(
            category_id=data.category_id,
            keyword=data.keyword.lower()
        )

        db.add(kw)
        await db.commit()

        return {"status": "ok"}