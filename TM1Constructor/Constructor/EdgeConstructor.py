from typing import Union, List
from TM1py.Utils import CaseAndSpaceInsensitiveTuplesDict

from TM1Constructor.Model.EdgeModel import EdgeModel


class EdgeConstructor:

    def __init__(self) -> None:
        pass

    def create(self, edge: Union[EdgeModel, dict]) -> CaseAndSpaceInsensitiveTuplesDict:
        """Create an CaseAndSpaceInsensitiveTuplesDict object from a expected EdgeModel.

        Args:
        -----
            edge (Union[EdgeModel, dict]): A EdgeModel or a dict based on EdgeModel

        Returns:
        --------
            CaseAndSpaceInsensitiveTuplesDict: A CaseAndSpaceInsensitiveTuplesDict TM1py object.
        """
        edge = self.__change_istance_if_dict(edge=edge)


        edge_object = CaseAndSpaceInsensitiveTuplesDict(
            {
                (edge.ParentName, edge.ComponentName): edge.Weight
            }
        )

        return edge_object

    def create_from_list(self, edges: List[Union[EdgeModel, dict]]) -> CaseAndSpaceInsensitiveTuplesDict:
        """Create a CaseAndSpaceInsensitiveTuplesDict objects from a expected EdgeModel.

        Args:
        -----
            edges (List[Union[HierarchyModel, dict]]): A list of EdgeModel or a dict based on EdgeModel

        Returns:
        --------
            CaseAndSpaceInsensitiveTuplesDict: A CaseAndSpaceInsensitiveTuplesDict TM1py object.
        """
        edge_objects = {}
        for edge in edges:
            edge_objects.update(self.create(edge))
            
        return edge_objects

    def __check_instance(self, edge: Union[EdgeModel, dict]) -> bool:
        return isinstance(edge, EdgeModel)
    
    def __change_istance_if_dict(self, edge: Union[EdgeModel, dict]) -> EdgeModel:
        if self.__check_instance(edge):
            return edge
        else:
            return EdgeModel(**edge)