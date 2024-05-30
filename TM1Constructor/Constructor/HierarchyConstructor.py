from typing import Union, List
from TM1py import Hierarchy

from TM1Constructor.Constructor.ElementConstructor import ElementConstructor
from TM1Constructor.Constructor.EdgeConstructor import EdgeConstructor
from TM1Constructor.Constructor.SubsetConstructor import SubsetConstructor
from TM1Constructor.Model.HierarchyModel import HierarchyModel

class HierarchyConstructor:
    
    def __init__(self) -> None:
        self.edge = EdgeConstructor()
        self.element = ElementConstructor()
        self.subset = SubsetConstructor()

        pass
    
    def create(self, dimension_name: str, hierarchy: Union[HierarchyModel, dict]) -> Hierarchy:
        """Create an hierarchy object from a expected HierarchyModel.

        Args:
        -----
            dimension_name (str): Dimension name of subset
            hierarchy (Union[HierarchyModel, dict]): A HierarchyModel or a dict based on HierarchyModel

        Returns:
        --------
            Hierarchy: A Hierarchy TM1py object.
        """
        if not isinstance(hierarchy, HierarchyModel):
            hierarchy = HierarchyModel(**hierarchy)
        
        hierarchy_object = Hierarchy(
            name=hierarchy.Name,
            dimension_name=dimension_name,
            elements=self.element.create_from_list(hierarchy.Elements),
            edges=self.edge.create_from_list(hierarchy.Edges),
            subsets=self.subset.create_from_list(
                dimension_name=dimension_name,
                hierarchy_name=hierarchy.Name,
                subsets=hierarchy.Subsets),
        )
        
        return hierarchy_object
    
    def create_from_list(self, dimension_name: str, hierarchies: List[Union[HierarchyModel, dict]]) -> List[Hierarchy]:
        """Create a list of hierarchy objects from a expected HierarchyModel.

        Args:
        -----
            dimension_name (str): Dimension name of subset
            hierarchies (List[Union[HierarchyModel, dict]]): A list of HierarchyModel or a dict based on HierarchyModel

        Returns:
        --------
            List[Hierarchy]: List of Hierarchy TM1py object.
        """
        
        return [self.create(dimension_name=dimension_name, hierarchy=hierarchy) for hierarchy in hierarchies]