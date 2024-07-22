from typing import Union
from typing import List

from TM1py import ElementAttribute

from TM1Constructor.model.ElementAttributeModel import ElementAttributeModel


class ElementAttributeConstructor:
    """A element attribute constructor class representation.
    """
    
    def __init__(self) -> None:
        pass


    def create(self, element_attribute: Union[ElementAttributeModel, dict]) -> ElementAttribute:
        """Create an element object from a dict.

        Args:
        -----
            element_attribute (Union[ElementAttributeModel, dict]): A ElementAttributeModel or a dict based on ElementAttributeModel

        Returns:
        --------
            ElementAttribute: A ElementAttribute TM1py object.
        """
        element_attribute: ElementAttributeModel = self.__change_istance_if_dict(element_attribute)
        
        element_attribute_object = ElementAttribute(
            name=element_attribute.Name,
            attribute_type=element_attribute.Type
        )
        
        return element_attribute_object


    def create_from_list(self, element_attributes: List[Union[ElementAttributeModel, dict]]) -> List[ElementAttribute]:
        """Create a list of element attribute objects from a expected ElementAttributeModel.

        Args:
        ----
            element_attributes (List[Union[ElementAttributeModel, dict]]): A list of ElementAttributeModel or a dict based on ElementAttributeModel

        Returns:
        --------
            List[ElementAttribute]: List of ElementAttribute TM1py object.
        """

        return [self.create(element_attribute=element_attribute) for element_attribute in element_attributes]


    def __check_instance(self, element_attribute: Union[ElementAttributeModel, dict]) -> bool:
        return isinstance(element_attribute, ElementAttributeModel)


    def __change_istance_if_dict(self, element_attribute: Union[ElementAttributeModel, dict]) -> ElementAttributeModel:
        if self.__check_instance(element_attribute):
            return element_attribute
        else:
            return ElementAttributeModel(**element_attribute)
