from TM1Constructor.Constructor import DimensionConstructor, SubsetConstructor, CubeConstructor, \
                                       HierarchyConstructor, ElementConstructor

class ObjectConstructor:
    
    def __init__(self) -> None:
        self.cube = CubeConstructor()
        self.dimension = DimensionConstructor()
        self.hierarchy = HierarchyConstructor()
        self.element = ElementConstructor()
        self.subset = SubsetConstructor()

