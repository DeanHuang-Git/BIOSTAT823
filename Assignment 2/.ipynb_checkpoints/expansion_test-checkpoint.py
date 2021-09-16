import unittest

from pi_expansion import pi_expansion
from mpmath import mp


class TestExpansion(unittest.TestCase):
    def test_list_int(self):
        """
        Test that check the expansion results
        """
        result = pi_expansion(4, mp.pi)
        result2 = pi_expansion(1, 4.051789120)
        result3 = pi_expansion(4, 4)
        result4 = pi_expansion(10, 700.05681205)
        result5 = pi_expansion(4, -644.55)
        self.assertEqual(str(result), '3.142')
        self.assertEqual(str(result2), '4.')
        self.assertEqual(str(result3), '4.000')
        self.assertEqual(str(result4), '700.0568120')
        self.assertEqual(str(result5), '-644.5')

if __name__ == '__main__':
    unittest.main()