import sys
import os
import unittest

from TM1py.Utils import CaseAndSpaceInsensitiveTuplesDict

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TM1Constructor.Constructor.DimensionConstructor import DimensionConstructor
from TM1Constructor.Model.DimensionModel import DimensionModel

class TestDimensionConstructor(unittest.TestCase):
    
    def setUp(self):
        self.constructor = DimensionConstructor()

    def test_create_dict_happy_case(self):
        dimension_dict = {
            "Name": "Dimension_Test",
            "Caption": {
                "pt": "Teste",
                "en": "Test"
            },
            "Attributes": [
                {
                    "Name": "Caption",
                    "Type": "Alias"
                },
                {
                    "Name": "Format",
                    "Type": "String"
                },
                {
                    "Name": "Test_Numeric",
                    "Type": "Numeric"
                }
            ],
            "Hierarchies": [
                {
                    "Name": "Dimension_Test",
                    "Elements": [
                        {
                            "Name": "element1",
                            "Type": "Numeric",
                            "Attributes": {
                                "Caption": {
                                    "pt": "teste",
                                    "en": "test"
                                },
                                "Format": "\\d"
                            }
                        },
                        {
                            "Name": "element2",
                            "Type": "Consolidated",
                            "Attributes": {}
                        }
                    ],
                    "Edges": [
                        {
                            "ParentName": "element2",
                            "ComponentName": "element1",
                            "Weight": 1
                        }
                    ],
                    "Subsets": [
                        {
                            "Name": "Test_Subset",
                            "MDX": "{[Dimension_Test].[Dimension_Test].MEMBERS}",
                            "Elements": [],
                            "Alias": "",
                            "Default": False
                        }
                    ]
                }
            ]
        }
        
        dimension = self.constructor.create(dimension=dimension_dict)
        
        self.assertIsInstance(dimension, DimensionModel)

    # def test_create_model_happy_case(self):
    #     dimension_model = DimensionModel()
        
    #     dimension = self.constructor.create(
    #         edge=dimension_model
    #     )
        
    #     self.assertIsInstance(edge, CaseAndSpaceInsensitiveTuplesDict)

if __name__ == '__main__':
    unittest.main()