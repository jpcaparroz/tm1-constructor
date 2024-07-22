from pydantic import BaseModel
from typing import List

from TM1Constructor.model.HierarchyModel import HierarchyModel
from TM1Constructor.model.ElementAttributeModel import ElementAttributeModel
from TM1Constructor.model.CaptionModel import CaptionModel


class DimensionModel(BaseModel):
    Name: str
    Caption: CaptionModel
    Attributes: List[ElementAttributeModel]
    Hierarchies: List[HierarchyModel]