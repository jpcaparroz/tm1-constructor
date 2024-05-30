from typing import Union, List
from TM1py import Element

from TM1Constructor.Model.ElementModel import ElementModel

class ElementConstructor:
    
    def __init__(self) -> None:
        pass
    
    def create(self, element: Union[ElementModel, dict]) -> Element:
        """Create an element object from a dict.

        Args:
        -----
            element_dict (dict): Element dict

        Returns:
        --------
            Element: A Element TM1py object.
        """
        if not isinstance(element, ElementModel):
            element = ElementModel(**element)
        
        element_object = Element(
            name=element.Name,
            element_type=element.Type
        )
        
        return element_object
    
    def create_from_list(self, elements: List[Union[ElementModel, dict]]) -> List[Element]:
        """Create a list of element objects from a expected ElementModel.

        Args:
        ----
            elements (List[Union[ElementModel, dict]]): A list of ElementModel or a dict based on ElementModel

        Returns:
        --------
            List[Element]: List of Element TM1py object.
        """
        
        return [self.create(element=element) for element in elements]