from TM1Constructor.Constructor.CubeConstructor import CubeConstructor
from TM1Constructor.Constructor.DimensionConstructor import DimensionConstructor
from TM1Constructor.Constructor.HierarchyConstructor import HierarchyConstructor
from TM1Constructor.Constructor.ElementConstructor import ElementConstructor
from TM1Constructor.Constructor.SubsetConstructor import SubsetConstructor

class ObjectConstructor:
    
    def __init__(self) -> None:
        self.cube = CubeConstructor()
        self.dimension = DimensionConstructor()
        self.hierarchy = HierarchyConstructor()
        self.element = ElementConstructor()
        self.subset = SubsetConstructor()

