from TM1py import Element

class ElementConstructor:
    
    def __init__(self) -> None:
        pass
    
    def create_from_dict(self, element_dict: dict) -> Element:
        """Create an element object from a dict.

        Args:
            element_dict (dict): Element dict

        Returns:
            Element: A Element TM1py object.
        """
        element_object = Element(
            name=element_dict['Name'],
            element_type=element_dict['Type']
        )
        
        return element_object