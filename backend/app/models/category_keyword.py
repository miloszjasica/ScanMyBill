from sqlalchemy import Column, String, Integer, ForeignKey
from app.db.base import Base


class CategoryKeyword(Base):
    __tablename__ = "category_keywords"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    keyword = Column(String, index=True)
    label = Column(String, nullable=True)