from pydantic import BaseModel
from typing import Optional, List


class UserOut(BaseModel):
    email: str
    deposit: float
    game_history: Optional[List] = []
