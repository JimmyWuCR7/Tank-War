## @file highSpeedTankTest.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief High Speed Tank Test Module
#  @date 04/04/2020

import sys
sys.path.append("../src")
import unittest
import pygame
from Map import CoordinateT
from highSpeedTank import highSpeedTank


## @brief Unit test for highSpeedTank module.
#  @detail This class do the unit test cases for part of the functions in
#  the highSpeedTank module, and it passes once all the outputs are the same
#  as the expected ones.
class HighSpeedTankTest(unittest.TestCase):

    ## @brief Test if the leap_start function in highSpeedTank module
    #  works properly.
    def test_highspeedtank_leap_start(self):
        resolution = 630, 630
        pygame.display.set_mode(resolution)
        tank = highSpeedTank(CoordinateT(8, 24))
        speed1 = tank.speed
        tank.leap_start()
        self.assertEqual((tank.speed - speed1), 3, "test_leap_start")
        pygame.quit()

    ## @brief Test if the leap_end function in highSpeedTank module works
    #   properly.
    def test_highspeedtank_leap_end(self):
        resolution = 630, 630
        pygame.display.set_mode(resolution)
        tank = highSpeedTank(CoordinateT(8, 24))
        tank.leap_start()
        tank.leap_end()
        self.assertEqual(tank.speed, 3, "test_leap_end")
        pygame.quit()


# Run the tests
if __name__ == '__main__':
    unittest.main()
