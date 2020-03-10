
import unittest
from python_challenge import *

class TestEncodeCard(unittest.TestCase):

    def test_encode(self):
        self.assertEqual(int(0b1000000000000100101100100101), encode_card("KD"), "Should be equal")
        self.assertEqual(int(0b10000001001100000111), encode_card("5S"), "Should be equal")
        self.assertEqual(int(0b10000000001000100100011101), encode_card("JC"), "Should be equal")



if __name__ == '__main__':
    unittest.main()
