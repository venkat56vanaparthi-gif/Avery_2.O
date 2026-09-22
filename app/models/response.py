from pydantic import BaseModel
from typing import Any, Optional


class JSONRPCResponse(BaseModel):

    jsonrpc: str = "2.0"

    id: int | str

    result: Optional[Any] = None

    error: Optional[dict] = None