"""
Questo modulo contiene le definizioni, sottoforma di classi, delle tabelle presenti nel database.
"""
import datetime

from sqlalchemy import Integer, String, LargeBinary, Column, Boolean, ForeignKey, Float, DateTime, Enum, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

import uuid
from backend.database.db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=False)
    password = Column(LargeBinary, nullable=False)

