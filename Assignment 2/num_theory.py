import unittest
from itertools import islice
from num_theory import num_theory
from window import window
from pi_expansion import pi_expansion
from mpmath import mp
from my_prime import prime

class TestNum_Theory(unittest.TestCase):
    def test_list_int(self):
        """
        Test that check where output of number theory function is correct
        """
        result = num_theory(100, 4, mp.pi)
        result2 = num_theory(100, 2, mp.pi)
        result3 = num_theory(100, 1, mp.pi)
        result4 = num_theory(100, 3, mp.pi)
        self.assertEqual(result, 4159)
        self.assertEqual(result2, 41)
        self.assertEqual(result3, 5)
        self.assertEqual(result4, 653)

if __name__ == '__main__':
    unittest.main()