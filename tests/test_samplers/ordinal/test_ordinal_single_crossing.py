from unittest import TestCase

from prefsampling.ordinal.singlecrossing import SingleCrossingNode


class TestOrdinalSingleCrossing(TestCase):
    def test_ordinal_single_crossing_node(self):
        n = SingleCrossingNode((0, 1, 2))
        n.__repr__()
        n.__str__()
        self.assertTrue(n.count_elections(0) == 0)
        self.assertTrue(n.count_elections(1) == 1)
        with self.assertRaises(ValueError):
            n.count_elections(-1)
