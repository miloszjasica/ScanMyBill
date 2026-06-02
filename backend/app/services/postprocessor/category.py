from sqlalchemy.future import select
from app.db.session import SessionLocal
from app.models.category import Category
from app.models.category_keyword import CategoryKeyword


async def assign_category(db, name: str):

    text = name.lower()

    result = await db.execute(
        select(Category, CategoryKeyword)
        .join(CategoryKeyword, Category.id == CategoryKeyword.category_id)
    )

    rows = result.all()

    for category, kw in rows:
        if kw.keyword in text:
            return category.name

    return "INNE"