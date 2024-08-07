from typing import Union
from typing import List

from TM1py import Subset

from TM1Constructor.model.SubsetModel import SubsetModel


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
        subset: SubsetModel = self.__change_istance_if_dict(subset)

        subset_object = Subset(
            subset_name=subset.Name,
            dimension_name=dimension_name,
            hierarchy_name=hierarchy_name,
            alias=subset.Alias,
            expression=subset.MDX,
            elements=[element for element in subset.Elements] if subset.Elements is not None else None
            )
        
        return subset_object


    def create_from_list(self, dimension_name: str, hierarchy_name:str, subsets: List[Union[SubsetModel, dict]]) -> List[Subset]:
        """Create a list of subset objects from a expected SubsetModel.

        Args:
        -----
            dimension_name (str): Dimension name of subset
            hierarchy_name (str): Hierarchy name of subset
            subsets (List[Union[SubsetModel, dict]]): A list of SubsetModel or a dict based on SubsetModel

        Returns:
        --------
            List[Subset]: List of Subset TM1py object.
        """

        return [self.create(dimension_name=dimension_name, hierarchy_name=hierarchy_name, subset=subset) for subset in subsets]


    def __check_instance(self, subset: Union[SubsetModel, dict]) -> bool:
        return isinstance(subset, SubsetModel)


    def __change_istance_if_dict(self, subset: Union[SubsetModel, dict]) -> SubsetModel:
        if self.__check_instance(subset):
            return subset
        else:
            return SubsetModel(**subset)
