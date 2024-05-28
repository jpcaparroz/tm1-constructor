from typing import Union
from TM1py import Element

from TM1Constructor.Model import ElementModel

class ElementConstructor:
    
    def __init__(self) -> None:
        pass
    
    def create(self, element: Union[ElementModel, dict]) -> Element:
        """Create an element object from a dict.

        Args:
            element_dict (dict): Element dict

        Returns:
            Element: A Element TM1py object.
        """
        if not isinstance(element, ElementModel):
            element = ElementModel(**element)
        
        element_object = Element(
            name=element.Name,
            element_type=element.Type
        )
        
        return element_object
    
    def create_from_list(self, element_list: list[ElementModel]) -> list[Element]:
        elements = []
        
        
        return elements