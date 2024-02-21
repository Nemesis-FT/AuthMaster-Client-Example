from backend.schemas import base

__all__ = (
    "RESTErrorModel",
)


class RESTErrorModel(base.RESTModel):
    """
    Model for errors returned by the API.
    """

    error_code: str
    reason: str

    class Config(base.RESTModel.Config):
        schema_extra = {
            "example": {
                "error_code": "NOT_FOUND",
                "reason": "The requested object was not found.",
            },
        }
