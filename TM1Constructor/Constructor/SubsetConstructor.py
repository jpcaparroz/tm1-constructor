from typing import Union
from TM1py import Subset

from TM1Constructor.Model.SubsetModel import SubsetModel

class SubsetConstructor:
    """A subset constructor class representation.
    """
    def __init__(self) -> None:
        pass
    
    def create(self, dimension_name: str, hierarchy_name:str, subset: Union[SubsetModel, dict]) -> Subset:
        """Create an subset object from a expected SubsetModel.

        Args:
        -----
            dimension_name (str): Dimension name of subset
            hierarchy_name (str): Hierarchy name of subset
            subset (Union[SubsetModel, dict]): A SubsetModel or a dict based on SubsetModel

        Returns:
        --------
            Subset: A Subset TM1py object.
        """
        
        if not isinstance(subset, SubsetModel):
            subset = SubsetModel(**subset)

        subset_object = Subset(
            subset_name=subset.Name,
            dimension_name=dimension_name,
            hierarchy_name=hierarchy_name,
            alias=subset.Alias,
            expression=subset.MDX,
            elements=[element for element in subset.Elements] if subset.Elements is not None else None
            )
        
        return subset_object
    
    def create_from_list(self, dimension_name: str, hierarchy_name:str, subsets: list[Union[SubsetModel, dict]]) -> list[Subset]:
        """Create a list of subset objects from a expected SubsetModel.

        Args:
        -----
            dimension_name (str): Dimension name of subset
            hierarchy_name (str): Hierarchy name of subset
            subsets (list[Union[SubsetModel, dict]]): A list of SubsetModel or a dict based on SubsetModel

        Returns:
        --------
            list[Subset]: List of Subset TM1py object.
        """
        
        return [self.create(dimension_name=dimension_name, hierarchy_name=hierarchy_name, subset=subset) for subset in subsets]