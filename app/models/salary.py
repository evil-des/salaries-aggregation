from datetime import datetime
from typing import List, Optional, Union
from bson import ObjectId
from enum import Enum

from .base import BaseModel


class Salary(BaseModel):
    id: str
    dt: datetime
    value: int


class GroupType(str, Enum):
    HOUR: str = "hour"
    DAY: str = "day"
    MONTH: str = "month"


class InputData(BaseModel):
    dt_from: datetime
    dt_upto: datetime
    group_type: GroupType

    class Config:
        use_enum_values = True
