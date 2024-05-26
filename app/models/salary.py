from datetime import datetime
from typing import List, Optional
from bson import ObjectId

from .base import BaseModel


class Salary(BaseModel):
    id: str
    dt: datetime
    value: int
