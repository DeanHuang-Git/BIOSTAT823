import unittest

from my_prime import prime


class TestPrime(unittest.TestCase):
    def test_list_int(self):
        """
        Test that check where the inputs are prime numbers
        """
        result = [prime(-1), prime(0), prime(1), prime(6), prime(100), prime(144), prime(1000)]
        result2 = [prime(2), prime(3), prime(5), prime(7), prime(29), prime(97), prime(7919)]
        self.assertEqual(not any(result), True)
        self.assertEqual(all(result2), True)

if __name__ == '__main__':
    unittest.main()