"""
Questo modulo contiene delle funzioni rapide per eseguire operazioni semplici con il db.
"""

__all__ = (
    "quick_create",
    "quick_retrieve",
    "quick_update",
)

import typing as t

import pydantic
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

import errors as errors

DatabaseObject = t.TypeVar("DatabaseObject")
PydanticObject = t.TypeVar("PydanticObject")


def quick_create(session: Session, obj: DatabaseObject) -> DatabaseObject:
    """
    Aggiungi un oggetto alla sessione, committalo e refreshalo per poi restituirlo
    :param session: La sessione del db.
    :param obj: L'oggetto da salvare.
    :return: L'oggetto finale.
    """

    session.add(obj)
    session.commit()
    session.refresh(obj)  # Utile per trigger e simili
    return obj


def quick_retrieve(session: Session, table: t.Type[DatabaseObject], **filters) -> DatabaseObject:
    """
    Interroga il database con diversi filtri
    :param session: La sessione del db.
    :param table: La tabella su cui cercare.
    :param filters: I filtri da utilizzare.
    :raise fastapi.HTTPException: Restituisce ``404 Not Found`` se non viene trovato nulla, e un ``500 Internal Server Error`` se vengono trovati più oggetti.
    :return: The retrieved object.
    """
    result = session.execute(
        select(table).filter_by(**filters)
    ).scalar()
    if not result:
        raise errors.ResourceNotFound()
    return result


def quick_update(session: Session, obj: DatabaseObject, data: pydantic.BaseModel) -> DatabaseObject:
    """
    Applica le modifiche contenute dentro il modello :mod:`pydantic`, poi le committa e restituisce l'oggetto dopo un refresh.
    :param session: La sessione del db.
    :param obj: L'oggetto da aggiornare.
    :param data: I dati con cui aggiornare l'oggetto.
    :return: L'oggetto aggiornato.
    """

    for key, value in data.dict().items():
        setattr(obj, key, value)

    session.commit()
    session.refresh(obj)
    return obj
