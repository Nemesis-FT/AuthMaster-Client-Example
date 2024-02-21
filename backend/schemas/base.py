"""
Questo modulo contiene la definizione degli schemi base, orm e non.
"""
from __future__ import annotations

import abc
import datetime
import uuid

import pydantic

import backend.database.models
import backend.database.enums

__all__ = (
    "RESTModel",
    "RESTORMModel",
)


class RESTModel(pydantic.BaseModel, metaclass=abc.ABCMeta):

    class Config(pydantic.BaseModel.Config):
        json_encoders = {
            uuid.UUID:
                lambda obj: str(obj),
            datetime.datetime:
                lambda obj: obj.timestamp(),
        }


class RESTORMModel(RESTModel, metaclass=abc.ABCMeta):

    class Config(RESTModel.Config):
        orm_mode = True