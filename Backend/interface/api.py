from typing import List
from pydantic import BaseModel


class DataItem(BaseModel):
    id: int
    gold: int


class DataList(BaseModel):
    items: List[DataItem]
