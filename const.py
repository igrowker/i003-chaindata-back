from enum import Enum
from typing import (
    Final,
    List,
)

OPEN_API_TITLE: Final = "API Chaindata"
OPEN_API_DESCRIPTION: Final = "Demo API over Postgres database built with FastAPI."
VERSION: Final = "v1.0.0"

PATH_USERS: Final = "/users"
TAG_USERS: Final[List[str | Enum] | None]  = ["Users"]

