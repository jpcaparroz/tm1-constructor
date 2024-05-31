import sys
import os
import unittest

from TM1py.Utils import CaseAndSpaceInsensitiveTuplesDict

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TM1Constructor.Constructor.EdgeConstructor import EdgeConstructor
from TM1Constructor.Model.EdgeModel import EdgeModel

class TestEdgeConstructor(unittest.TestCase):
    
    def setUp(self):
        self.constructor = EdgeConstructor()

    def test_create_dict_happy_case(self):
        edge_dict = {
            "ParentName": "total_example",
            "ComponentName": "leaf_example",
            "Weight": 1
        }
        
        edge = self.constructor.create(
            edge=edge_dict
        )
        
        self.assertIsInstance(edge, CaseAndSpaceInsensitiveTuplesDict)

    def test_create_model_happy_case(self):
        edge_model = EdgeModel(ParentName='total_example', ComponentName='leaf_example', Weight=1)
        
        edge = self.constructor.create(
            edge=edge_model
        )
        
        self.assertIsInstance(edge, CaseAndSpaceInsensitiveTuplesDict)

if __name__ == '__main__':
    unittest.main()