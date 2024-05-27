from TM1Constructor.Constructor import DimensionConstructor, SubsetConstructor, CubeConstructor, HierarchyConstructor

class ObjectConstructor:
    
    def __init__(self, **kwargs) -> None:
        self.cube = CubeConstructor()
        self.dimension = DimensionConstructor()
        self.hierarchy = HierarchyConstructor()
        self.subset = SubsetConstructor()

