from pydantic import BaseModel
from typing import List

from TM1Constructor.model.ElementModel import ElementModel
from TM1Constructor.model.EdgeModel import EdgeModel
from TM1Constructor.model.SubsetModel import SubsetModel


class HierarchyModel(BaseModel):
    Name: str
    Elements: List[ElementModel]
    Edges: List[EdgeModel]
    Subsets: List[SubsetModel]