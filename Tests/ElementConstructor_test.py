import sys
import os
import unittest

from TM1py.Objects import Element

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TM1Constructor.Constructor import ObjectConstructor

class TestElementConstructor(unittest.TestCase):
    
    def setUp(self):
        self.constructor = ObjectConstructor()

    def test_create_happy_case(self):
        element_model = {
            "Name": "Element_Test",
            "Type": "NUMERIC"
        }
        
        element = self.constructor.element.create(
            element=element_model
        )
        
        self.assertIsInstance(element, Element)
        self.assertEqual(element_model['Name'], element.name)
        self.assertEqual(element_model['Type'], element.element_type.name)

    def test_create_from_list_happy_case(self):
        element_models = [
            {"Name": "Element_Test_1", "Type": "NUMERIC"},
            {"Name": "Element_Test_2", "Type": "STRING"},
            {"Name": "Element_Test_3", "Type": "CONSOLIDATED"}
        ]
        
        elements = self.constructor.element.create_from_list(
            elements=element_models
        )

        self.assertEqual(len(element_models), len(elements))

if __name__ == '__main__':
    unittest.main()