import sys
import os
import unittest

from TM1py.Objects import Subset

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TM1Constructor.constructor.SubsetConstructor import SubsetConstructor

class TestSubsetConstructor(unittest.TestCase):
    
    def setUp(self):
        self.constructor = SubsetConstructor()
        self.dimension_name = 'Test_Dimension'
        self.hierarchy_name = 'Test_Hierarchy'

    def test_create_happy_case(self):
        subset_model = {
            "Name": "TestSubset",
            "MDX": "SELECT {TM1SUBSETALL([Dimension])} ON ROWS FROM [Cube]",
            "Elements": None,
            "Alias": "Caption",
            "Default" : False
        }
        
        subset = self.constructor.create(
            dimension_name=self.dimension_name,
            hierarchy_name=self.hierarchy_name,
            subset=subset_model
        )
        
        self.assertIsInstance(subset, Subset)

    def test_create_with_mdx(self):
        subset_model = {
            "Name": "TestSubset",
            "MDX": "SELECT {TM1SUBSETALL([Dimension])} ON ROWS FROM [Cube]",
            "Elements": None,
            "Alias": None,
            "Default" : False
        }
        
        subset = self.constructor.create(
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
        
        self.assertRaises(TypeError, lambda: self.constructor.create(hierarchy_name=self.hierarchy_name, 
                                                                                      subset=subset_model))

    def test_create_without_hierarchy_name(self):
        subset_model = {
            "Name": "TestSubset",
            "MDX": "SELECT {TM1SUBSETALL([Dimension])} ON ROWS FROM [Cube]",
            "Elements": None,
            "Alias": None,
            "Default" : False
        }
        
        self.assertRaises(TypeError, lambda: self.constructor.create(dimension_name=self.dimension_name, 
                                                                                      subset=subset_model))

if __name__ == '__main__':
    unittest.main()