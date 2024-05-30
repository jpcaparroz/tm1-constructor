from pydantic import BaseModel
from typing import List

from TM1Constructor.Model.ElementModel import ElementModel
from TM1Constructor.Model.EdgeModel import EdgeModel
from TM1Constructor.Model.SubsetModel import SubsetModel

class HierarchyModel(BaseModel):
    Name: str
    Elements: List[ElementModel]
    Edges: List[EdgeModel]
    Subsets: List[SubsetModel]