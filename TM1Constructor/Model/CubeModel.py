from pydantic import BaseModel
from typing import List

from TM1Constructor.Model.ViewModel import ViewModel

class CubeModel(BaseModel):
    Name: str
    Rules: str
    Attributes: int
    Dimensions: List[str]
    Views: List[ViewModel]