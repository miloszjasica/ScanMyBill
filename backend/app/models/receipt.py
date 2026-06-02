from sqlalchemy import Column, String, Numeric, DateTime, func
from app.db.base import Base

class Receipt(Base):
    __tablename__ = "receipts"

    id = Column(String, primary_key=True)
    merchant = Column(String, nullable=True)
    total = Column(Numeric, nullable=True)
    raw_text = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())