import sys
import os
import unittest

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TM1Constructor.Constructor import ObjectConstructor

class TestSubsetConstructor(unittest.TestCase):
    
    def setUp(self):
        self.constructor = ObjectConstructor()
        self.dimension_name = 'Test_Dimension'
        self.hierarchy_name = 'Test_Hierarchy'

    def test_create_with_mdx(self):
        subset_model = {
            "Name": "TestSubset",
            "MDX": "SELECT {TM1SUBSETALL([Dimension])} ON ROWS FROM [Cube]",
            "Elements": None,
            "Alias": None,
            "Default" : False
        }
        
        subset = self.constructor.subset.create(
            dimension_name=self.dimension_name,
            hierarchy_name=self.hierarchy_name,
            subset=subset_model
        )
        
        self.assertEqual(subset.name, 'TestSubset')
        self.assertEqual(subset.dimension_name, self.dimension_name)
        self.assertEqual(subset.hierarchy_name, self.hierarchy_name)
        self.assertEqual(subset.expression, 'SELECT {TM1SUBSETALL([Dimension])} ON ROWS FROM [Cube]')
        self.assertFalse(subset.elements)
        self.assertIsNone(subset.alias)

    def test_create_without_dimension_name(self):
        subset_model = {
            "Name": "TestSubset",
            "MDX": "SELECT {TM1SUBSETALL([Dimension])} ON ROWS FROM [Cube]",
            "Elements": None,
            "Alias": None,
            "Default" : False
        }
        
        self.assertRaises(TypeError, lambda: self.constructor.subset.create(hierarchy_name=self.hierarchy_name, 
                                                                                      subset=subset_model))

    def test_create_without_hierarchy_name(self):
        subset_model = {
            "Name": "TestSubset",
            "MDX": "SELECT {TM1SUBSETALL([Dimension])} ON ROWS FROM [Cube]",
            "Elements": None,
            "Alias": None,
            "Default" : False
        }
        
        self.assertRaises(TypeError, lambda: self.constructor.subset.create(dimension_name=self.dimension_name, 
                                                                                      subset=subset_model))

if __name__ == '__main__':
    unittest.main()