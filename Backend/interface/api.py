from typing import List
from pydantic import BaseModel


class DataItem(BaseModel):
    id: int
    money: int


class DataList(BaseModel):
    items: List[DataItem]
