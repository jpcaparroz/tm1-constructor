from typing import Union
from TM1py import Hierarchy

from TM1Constructor.Constructor.ElementConstructor import ElementConstructor
from TM1Constructor.Constructor.EdgeConstructor import EdgeConstructor
from TM1Constructor.Constructor.SubsetConstructor import SubsetConstructor
from TM1Constructor.Model import HierarchyModel

class HierarchyConstructor:
    
    def __init__(self) -> None:
        self.edge = EdgeConstructor()
        self.element = ElementConstructor()
        self.subset = SubsetConstructor()

        pass
    
    def create(self, dimension_name: str, hierarchy: Union[HierarchyModel, dict]) -> Hierarchy:

        if not isinstance(hierarchy, HierarchyModel):
            hierarchy = HierarchyModel(**hierarchy)
        
        hierarchy_object = Hierarchy(
            name=hierarchy.Name,
            dimension_name=dimension_name,
            elements=self.element.create_from_list(hierarchy.Elements),
            edges=self.edge.create(hierarchy.Edges),
            subsets=self.subset.create_from_list(
                dimension_name=dimension_name,
                hierarchy_name=hierarchy.Name,
                subsets=hierarchy.Subsets),
        )
        
        return hierarchy_object