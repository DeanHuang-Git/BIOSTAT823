import unittest
from itertools import islice
from window import window


class TestWindow(unittest.TestCase):
    def test_list_int(self):
        """
        Test that check where output of window function is correct
        """
        result = window('75841', 2)
        result2 = window('8000', 1)
        self.assertEqual([i for i in result], [('7', '5'),
                                  ('5', '8'),
                                  ('8', '4'), 
                                  ('4', '1')])
        self.assertEqual([i for i in result2], [('8',),
                                  ('0',),
                                  ('0',), 
                                  ('0',)])

if __name__ == '__main__':
    unittest.main()