from pydantic import BaseModel
from typing import List

from TM1Constructor.Model.HierarchyModel import HierarchyModel
from TM1Constructor.Model.ElementAttributeModel import ElementAttributeModel

class DimensionModel(BaseModel):
    Name: str
    Attributes: List[ElementAttributeModel]
    Hierarchies: List[HierarchyModel]