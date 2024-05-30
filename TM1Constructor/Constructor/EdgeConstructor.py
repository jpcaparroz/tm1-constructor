from typing import Union
from TM1py.Utils import CaseAndSpaceInsensitiveTuplesDict

from TM1Constructor.Model.EdgeModel import EdgeModel


class EdgeConstructor:

    def __init__(self) -> None:
        pass

    def create(self, edges: list[Union[EdgeModel, dict]]) -> CaseAndSpaceInsensitiveTuplesDict:
        treated_edges = []
        for edge in edges:
            if not isinstance(edge, EdgeModel):
                treated_edges.append(EdgeModel(**edge))

        edge_objects = CaseAndSpaceInsensitiveTuplesDict(
            {
                (edge.ParentName, edge.ComponentName): edge.Weight
                for edge in treated_edges
            }
        )

        return edge_objects
