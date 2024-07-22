from typing import Union
from typing import List

from TM1py import Element

from TM1Constructor.model.ElementModel import ElementModel


class ElementConstructor:
    """A element constructor class representation.
    """
    
    def __init__(self) -> None:
        pass


    def create(self, element: Union[ElementModel, dict]) -> Element:
        """Create an element object from a dict.

        Args:
        -----
            element (Union[ElementModel, dict]): A ElementModel or a dict based on ElementModel

        Returns:
        --------
            Element: A Element TM1py object.
        """
        element = self.__change_istance_if_dict(element=element)
        
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


    def __check_instance(self, element: Union[ElementModel, dict]) -> bool:
        return isinstance(element, ElementModel)


    def __change_istance_if_dict(self, element: Union[ElementModel, dict]) -> ElementModel:
        if self.__check_instance(element):
            return element
        else:
            return ElementModel(**element)
