from typing import Union, List
from TM1py import TM1Service, Dimension

from TM1Constructor.Model.DimensionModel import DimensionModel
from TM1Constructor.Model.ElementAttributeModel import ElementAttributeModel
from TM1Constructor.Constructor.HierarchyConstructor import HierarchyConstructor
from TM1Constructor.Constructor.ElementAttributeConstructor import ElementAttributeConstructor

class DimensionConstructor:
    
    def __init__(self) -> None:
        pass
    
    def __init__(self) -> None:
        self.hierarchy = HierarchyConstructor()
        self.element_attribute = ElementAttributeConstructor()

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
        dimension = self.__change_istance_if_dict(dimension=dimension)
        
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
    
    def create_attributes(self, tm1_service: TM1Service, dimension: Union[DimensionModel, dict]):
        dimension = self.__change_istance_if_dict(dimension=dimension)
        
        for element_attribute in dimension.Attributes:
            return tm1_service.elements.create_element_attribute(dimension_name=dimension.Name, 
                                                                 hierarchy_name=dimension.Name, 
                                                                 element_attribute=self.element_attribute.create(element_attribute=element_attribute))
             
    def __check_instance(self, dimension: Union[DimensionModel, dict]) -> bool:
        return isinstance(dimension, DimensionModel)
    
    def __change_istance_if_dict(self, dimension: Union[DimensionModel, dict]) -> DimensionModel:
        if self.__check_instance(dimension):
            return dimension
        else:
            return DimensionModel(**dimension)