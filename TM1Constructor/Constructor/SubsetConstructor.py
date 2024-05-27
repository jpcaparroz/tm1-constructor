from TM1py import Subset

class SubsetConstructor:
    """A subset constructor class representation.
    """
    def __init__(self) -> None:
        pass
    
    def create_from_dict(self, dimension_name: str, hierarchy_name:str, subset_dict: dict) -> Subset:
        """Create an subset object from a dict.

        Args:
            dimension_name (str): Dimension name of subset
            hierarchy_name (str): Hierarchy name of subset
            subset_dict (dict): Subset dict

        Returns:
            Subset: A Subset TM1py object.
        """
        subset_object = Subset(
            subset_name=subset_dict['Name'],
            dimension_name=dimension_name,
            hierarchy_name=hierarchy_name,
            alias=subset_dict['Alias'],
            expression=subset_dict['MDX'],
            elements=[element for element in subset_dict['Elements']] if subset_dict['Elements'] is not None else None
            )
        
        return subset_object
