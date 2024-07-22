from typing import Union

from TM1py import Cube

from TM1Constructor.model.CubeModel import CubeModel

class CubeConstructor:
    """A cube constructor class representation.
    """

    def __init__(self) -> None:
        pass


    def create(self, cube: Union[CubeModel, dict]) -> Cube:
        """Create an cube object from a dict.

        Args:
        -----
            cube (Union[cube, dict]): A CubeModel or a dict based on CubeModel

        Returns:
        --------
            Cube: A Cube TM1py object.
        """
        cube: CubeModel = self.__change_istance_if_dict(cube)
        
        cube_object = Cube(
            name=cube.Name,
            dimensions=cube.Dimensions,
            rules=cube.Rules
        )

        return cube_object


    def __check_instance(self, cube: Union[CubeModel, dict]) -> bool:
        return isinstance(cube, CubeModel)


    def __change_istance_if_dict(self, cube: Union[CubeModel, dict]) -> CubeModel:
        if self.__check_instance(cube):
            return cube
        else:
            return CubeModel(**cube)
