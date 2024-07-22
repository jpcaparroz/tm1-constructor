from pydantic import BaseModel
from typing import List
from typing import Optional

from TM1Constructor.model.ViewModel import ViewModel
from TM1Constructor.model.ElementAttributeModel import ElementAttributeModel
from TM1Constructor.model.CaptionModel import CaptionModel


class CubeModel(BaseModel):
    Name: str
    Caption: CaptionModel
    Attributes: List[ElementAttributeModel]
    Dimensions: List[str]
    Rules: Optional[str]
    Views: List[ViewModel]