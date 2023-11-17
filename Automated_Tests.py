"""
Test_1 is designed to test functions within 'Preprocessing.py'
These are automated tests that test various inputs and outputs in the function
against requirements written in the test code.

Author:
Andrew Pfeiffer
11/15/2023
"""

import unittest
import random
from preprocessing import Word_to_ascii, Padding, Export_Block_To_File, ASCII_To_Binary


class TestWordToASCII(unittest.TestCase):

    # must be called 'test_...' to name the function within the class
    def test_single_word_conversion(self):
        """ Test a string input to expect ASCII output """
        result = Word_to_ascii("Hello")
        expected = "72 101 108 108 111 "
        self.assertEqual(result, expected)

    def test_special_characters(self):
        """ Test special character and expect no output. """
        result = Word_to_ascii("@#$()&")
        expected = ""
        self.assertEqual(result, expected)

    def test_numbers(self):
        """ Test a string of numbers and expect ASCII output. """
        result = Word_to_ascii("012100")
        expected = "48 49 50 49 48 48 "
        self.assertEqual(result, expected)


class TestAsciiToBinary(unittest.TestCase):

    def test_set_string_input(self):
        """
        Input ASCII values and expect output as 8 bit binary.
        """
        result = ASCII_To_Binary("91 89 74 67")
        expected = "01011011010110010100101001000011"
        self.assertEqual(result, expected)

    def test_empty_string(self):
        """ Test for an output of an empty string. """
        result = ASCII_To_Binary("")
        expected = ""
        self.assertEqual(result, expected)

    def test_random_ASCII_inputs(self):
        """ Test 100 random integers between 0 and 255. """
        for i in range(0, 100):
            num1 = random.randint(0, 255)
            num2 = random.randint(0, 255)
            num3 = random.randint(0, 255)
            result = ASCII_To_Binary(f"{num1} {num2} {num3}")
            expected = f"0{bin(num1)[2:]}0{bin(num2)[2:]}0{bin(num3)[2:]}"
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
