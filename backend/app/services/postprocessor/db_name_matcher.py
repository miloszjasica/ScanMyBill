from sqlalchemy.future import select
from app.db.session import SessionLocal
from app.models.category import Category
from app.models.category_keyword import CategoryKeyword


async def match_product(db, name: str):
    text = name.lower()

    result = await db.execute(
        select(
            Category.name,
            CategoryKeyword.keyword,
            CategoryKeyword.label
        ).join(CategoryKeyword)
    )

    rows = result.all()

    for category_name, keyword, label in rows:
        if keyword in text:
            return {
                "name": label or keyword,
                "category": category_name
            }

    return {
        "name": name,
        "category": "INNE"
    }