from typing import Union, List
from TM1py import Dimension

from TM1Constructor.Model.DimensionModel import DimensionModel
from TM1Constructor.Constructor.HierarchyConstructor import HierarchyConstructor

class DimensionConstructor:
    
    def __init__(self) -> None:
        pass
    
    def __init__(self) -> None:
        self.hierarchy = HierarchyConstructor()

        pass
    
    def create(self, dimension: Union[DimensionModel, dict]) -> Dimension:
        """Create an dimension object from a expected DimensionModel.

        Args:
        -----
            dimension (Union[DimensionModel, dict]): A DimensionModel or a dict based on DimensionModel

        Returns:
        --------
            Dimension: A Dimension TM1py object.
        """
        if not isinstance(dimension, DimensionModel):
            dimension = DimensionModel(**dimension)
        
        dimension_object = Dimension(
            name=dimension.Name,
            hierarchies=self.hierarchy.create_from_list(dimension_name=dimension.Name, hierarchies=dimension.Hierarchies)
        )
        
        return dimension_object
    
    def create_from_list(self, dimensions: List[Union[DimensionModel, dict]]) -> List[Dimension]:
        """Create a list of dimension objects from a expected DimensionModel.

        Args:
        -----
            dimensions (List[Union[DimensionModel, dict]]): A list of DimensionModel or a dict based on DimensionModel

        Returns:
        --------
            List[Dimension]: List of Dimension TM1py object.
        """
        
        return [self.create(dimension=dimension) for dimension in dimensions]