"""
Questo modulo contiene la definizione del DBMS utilizzato dall'applicazione e della sessione di collegamento.
"""
import typing as t
from os import environ

import lazy_object_proxy
import sqlalchemy.engine
import sqlalchemy.orm
from backend.configuration import DB_URI

# noinspection PyTypeChecker
from sqlalchemy.orm import declarative_base

engine: sqlalchemy.engine.Engine = lazy_object_proxy.Proxy(lambda: sqlalchemy.create_engine(DB_URI))
# noinspection PyTypeChecker
Session: t.Type[sqlalchemy.orm.Session] = lazy_object_proxy.Proxy(lambda: sqlalchemy.orm.sessionmaker(bind=engine))
Base = declarative_base()