from pydantic import BaseModel

from TM1Constructor.Model import ElementModel, EdgeModel, SubsetModel

class HierarchyModel(BaseModel):
    Name: str
    Elements: list[ElementModel]
    Edges: list[EdgeModel]
    Subsets: list[SubsetModel]