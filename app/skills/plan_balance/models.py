from pydantic import BaseModel
from typing import Optional


class PlanBalanceRequest(BaseModel):

    member_id: str
    accumulator: str


class PlanBalanceResponse(BaseModel):

    status: str
    member_id: Optional[str] = None
    accumulator: Optional[str] = None
    balance: Optional[float] = None
    message: Optional[str] = None