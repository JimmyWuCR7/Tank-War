## @file decTimeTest.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief decTime Test Module
#  @date 04/04/2020

import sys
sys.path.append("../src")
import unittest
import pygame
from decTime import decTime


## @brief Unit test for decTime module
#  @detail This class do the unit test cases for part of the functions in
#  the decTime module, and it passes once all the outputs are the same
#  as the expected ones.
class DecTimeTest(unittest.TestCase):

    ## @brief Test if the constructor in decTime module works properly.
    def test_dectime(self):
        time = decTime(0)
        self.assertEqual([time.hour, time.minute, time.second], [0, 0, 0],
                         "test_dectime")
        time = decTime(4000)
        self.assertEqual([time.hour, time.minute, time.second], [1, 6, 40],
                         "test_dectime")

    def test_subtime(self):
        time = decTime(30)
        time.subTime()
        self.assertEqual([time.hour, time.minute, time.second], [0, 0, 29],
                         "test_subtime")

        time = decTime(60)
        time.subTime()
        self.assertEqual([time.hour, time.minute, time.second], [0, 0, 59],
                         "test_subtime")

        time = decTime(3600)
        time.subTime()
        self.assertEqual([time.hour, time.minute, time.second], [0, 59, 59],
                         "test_subtime")

        time = decTime(36000)
        time.subTime()
        self.assertEqual([time.hour, time.minute, time.second], [9, 59, 59],
                         "test_subtime")


# Run the tests
if __name__ == '__main__':
    unittest.main()
