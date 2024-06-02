from pydantic import BaseModel
from typing import List

from TM1Constructor.Model.HierarchyModel import HierarchyModel
from TM1Constructor.Model.ElementAttributeModel import ElementAttributeModel
from TM1Constructor.Model.CaptionModel import CaptionModel

class DimensionModel(BaseModel):
    Name: str
    Caption: CaptionModel
    Attributes: List[ElementAttributeModel]
    Hierarchies: List[HierarchyModel]