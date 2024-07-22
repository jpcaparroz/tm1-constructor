from typing import Union
from typing import List

from TM1py import MDXView

from TM1Constructor.model.ViewModel import ViewModel


class ViewConstructor:
    """A view constructor class representation.
    """

    def __init__(self) -> None:
        pass


    def create(self, cube_name:str, view: Union[ViewModel, dict]) -> MDXView:
        """Create an MDXView object from a expected ViewModel.

        Args:
        -----
            view (Union[ViewModel, dict]): A ViewModel or a dict based on ViewModel

        Returns:
        --------
            MDXView: A MDXView TM1py object.
        """
        view: ViewModel = self.__change_istance_if_dict(view)

        view_object = MDXView(
            cube_name=cube_name,
            view_name=view.Name,
            MDX=view.MDX
        )

        return view_object


    def create_from_list(self, cube_name:str, views: List[Union[ViewModel, dict]]) -> List[MDXView]:
        """Create a MDXView objects from a expected ViewModel.

        Args:
        -----
            views (List[Union[ViewModel, dict]]): A list of ViewModel or a dict based on ViewModel

        Returns:
        --------
            MDXView: A MDXView TM1py object.
        """
        return [self.create(cube_name=cube_name, view=view) for view in views]


    def __check_instance(self, view: Union[ViewModel, dict]) -> bool:
        return isinstance(view, ViewModel)


    def __change_istance_if_dict(self, view: Union[ViewModel, dict]) -> ViewModel:
        if self.__check_instance(view):
            return view
        else:
            return ViewModel(**view)
