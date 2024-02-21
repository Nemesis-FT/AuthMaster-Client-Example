"""
Questo modulo contiene dipendenze comuni tra più moduli.
"""
import sqlalchemy
from backend.database.db import Session


def dep_dbsession() -> sqlalchemy.orm.Session:
    """
    Dipendenza che crea una nuova sessione di collegamento al database, la quale viene chiusa terminato il suo ciclo d'uso.
    """
    with Session(future=True) as session:
        yield session