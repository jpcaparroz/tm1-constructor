import unittest

from TM1Constructor.Constructor import ObjectConstructor
from TM1Constructor.Model import SubsetModel


class TestSubsetConstructor(unittest.TestCase):
    
    def setUp(self):
        self.constructor = ObjectConstructor.SubsetConstructor()

    def test_create_from_dict_with_mdx(self):
        subset_model = SubsetModel(
            Name='TestSubset',
            MDX='SELECT {TM1SUBSETALL([Dimension])} ON ROWS FROM [Cube]',
            Elements=None,
            Alias=None,
            Default=False
        )
        subset = self.constructor.create_from_dict(
            dimension_name='Dimension',
            hierarchy_name='Hierarchy',
            subset=subset_model
        )
        self.assertEqual(subset.subset_name, 'TestSubset')
        self.assertEqual(subset.dimension_name, 'Dimension')
        self.assertEqual(subset.hierarchy_name, 'Hierarchy')
        self.assertEqual(subset.expression, 'SELECT {TM1SUBSETALL([Dimension])} ON ROWS FROM [Cube]')
        self.assertIsNone(subset.elements)
        self.assertIsNone(subset.alias)

if __name__ == '__main__':
    unittest.main()