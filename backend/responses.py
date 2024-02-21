"""
Questo modulo contiene le risposte non-json dell'applicazione.
"""
import starlette.responses

NO_CONTENT = starlette.responses.Response(content=None, status_code=204)
