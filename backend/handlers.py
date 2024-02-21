"""
Questo modulo contiene tutti i gestori di errore per :mod:`fastapi`.
"""

import typing as t

import fastapi
import sqlalchemy.exc

import backend.errors as errors


# noinspection PyUnusedLocal
async def handle_acme_error(request: fastapi.Request, exc: errors.AcmedeliverException) -> fastapi.Response:
    return exc.to_response()


# noinspection PyUnusedLocal
async def handle_sqlalchemy_not_found(request: fastapi.Request, exc: sqlalchemy.exc.NoResultFound) -> t.NoReturn:
    raise errors.ResourceNotFound()


# noinspection PyUnusedLocal
async def handle_sqlalchemy_multiple_results(request: fastapi.Request, exc: sqlalchemy.exc.MultipleResultsFound) -> t.NoReturn:
    raise errors.MultipleResultsFound()


# noinspection PyUnusedLocal
async def handle_generic_error(request: fastapi.Request, exc: Exception) -> fastapi.Response:
    raise errors.AcmedeliverException()
