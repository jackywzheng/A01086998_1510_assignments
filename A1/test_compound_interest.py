from unittest import TestCase
import compound_interest


class TestCompoundInterest(TestCase):
    def test_compound_interest_middle(self):
        self.assertEqual(132664.88525722112, compound_interest.compound_interest(50000, 0.1, 2, 10))

    def test_compound_interest_small(self):
        self.assertEqual(10.1, compound_interest.compound_interest(10, 0.01, 1, 1))

    def test_compound_interest_large(self):
        self.assertEqual(3.881254963822318e+37, compound_interest.compound_interest(1000000, 5, 6, 20))

    def test_compound_interest_large_float(self):
        self.assertTrue(float, compound_interest.compound_interest(1000, 0.5, 1, 20))

