from pydantic import BaseModel
from typing import Optional


class JSONRPCRequest(BaseModel):

    jsonrpc: str = "2.0"

    id: int | str

    method: str

    params: dict = {}