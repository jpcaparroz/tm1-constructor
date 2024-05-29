from typing import Union
from TM1py import Hierarchy

from TM1Constructor.Constructor import ElementConstructor, SubsetConstructor
from TM1Constructor.Model import HierarchyModel

class HierarchyConstructor:
    
    def __init__(self) -> None:
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
            edges=hierarchy.edges.create_from_list(hierarchy.Edges),
            subsets=,
        )
        
        return ''