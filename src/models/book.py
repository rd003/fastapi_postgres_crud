from src.database.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column

class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    author: Mapped[str] = mapped_column(String(50))