from typing import Union
from requests import Response

from TM1py import TM1Service

from TM1Constructor.model.CaptionModel import CaptionModel


class CaptionConstructor:
    """A caption constructor class representation.
    """

    def __init__(self) -> None:
        pass


    def __check_instance(self, caption: Union[CaptionModel, dict]) -> bool:
        return isinstance(caption, CaptionModel)


    def __change_istance_if_dict(self, caption: Union[CaptionModel, dict]) -> CaptionModel:
        if self.__check_instance(caption):
            return caption
        else:
            return CaptionModel(**caption)


    async def create_for_cube(self, cube_name: str, 
                              caption: Union[CaptionModel, dict], tm1_service: TM1Service) -> Response:
        caption: CaptionModel = self.__change_istance_if_dict(caption)
        script: str = "CubeAttrInsert('', 'Caption', 'A');"

        for language, value in caption.model_dump().items():
            script += f"CubeAttrPutS('{value}', {cube_name}, 'Caption', '{language}');"

        async with TM1Service(tm1_service):          
            return await tm1_service.processes.execute_ti_code(script)


    async def create_for_dimension(self, dimension_name: str, 
                                   caption: Union[CaptionModel, dict], tm1_service: TM1Service) -> Response:
        caption: CaptionModel = self.__change_istance_if_dict(caption)
        script: str = "DimensionAttrInsert('', 'Caption', 'A');"

        for language, value in caption.model_dump().items():
            script += f"DimensionAttrPutS('{value}', {dimension_name}, 'Caption', '{language}');"

        async with TM1Service(tm1_service):          
            return await tm1_service.processes.execute_ti_code(script)


    async def create_for_hierarchy(self, dimension_name: str, hierarchy_name: str,
                                   caption: Union[CaptionModel, dict], tm1_service: TM1Service) -> Response:
        caption: CaptionModel = self.__change_istance_if_dict(caption)
        script: str = "DimensionAttrInsert('', 'Caption', 'A');"

        for language, value in caption.model_dump().items():
            script += f"HierarchyAttrPutS('{value}', {dimension_name}, {hierarchy_name}, 'Caption', '{language}');"

        async with TM1Service(tm1_service):          
            return await tm1_service.processes.execute_ti_code(script)


    async def create_for_subset(self, dimension_name: str, hierarchy_name: str,
                                caption: Union[CaptionModel, dict], tm1_service: TM1Service) -> Response:
        caption: CaptionModel = self.__change_istance_if_dict(caption)
        script: str = "DimensionAttrInsert('', 'Caption', 'A');"

        for language, value in caption.model_dump().items():
            script += f"HierarchyAttrPutS('{value}', {dimension_name}, {hierarchy_name}, 'Caption', '{language}');"

        async with TM1Service(tm1_service):          
            return await tm1_service.processes.execute_ti_code(script)