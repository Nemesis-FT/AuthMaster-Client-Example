"""
Questo modulo contiene le dipendenze legate agli utenti.
"""
from datetime import datetime

from fastapi import UploadFile
from sqlalchemy.orm import Session

from backend.database import models


def get_user(db: Session, uid: int):
    return db.query(models.User).filter(models.User.uid == uid).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session):
    return db.query(models.User).all()
