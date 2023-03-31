## @file doubleLifeTankTest.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief Double Life Tank Test Module
#  @date 04/04/2020

import sys
sys.path.append("../src")
import unittest
import pygame
from Map import CoordinateT
from doubleLifeTank import doubleLifeTank


## @brief Unit test for doubleLifeTank module.
#  @detail This class do the unit test cases for part of the functions in
#  the doubleLifeTank module, and it passes once all the outputs are the same
#  as the expected ones.
class doubleLifeTankTest(unittest.TestCase):

    ## @brief Test if the bulletproof_start function in doubleLifeTank
    #   module works properly.
    def test_doublelifetank_bulletproof_start(self):
        resolution = 630, 630
        pygame.display.set_mode(resolution)
        tank = doubleLifeTank(CoordinateT(8, 24))
        tank.bulletproof_start()
        self.assertEqual(tank.bulletProof, True, "test_bulletproof_start")
        pygame.quit()

    ## @brief Test if the bulletproof_end function in doubleLifeTank
    #   module works properly.
    def test_doublelifetank_bulletproof_end(self):
        resolution = 630, 630
        pygame.display.set_mode(resolution)
        tank = doubleLifeTank(CoordinateT(8, 24))
        tank.bulletproof_end()
        self.assertEqual(tank.bulletProof, False, "test_bulletproof_end")
        pygame.quit()

    ## @brief Test if the getBulletProof function in doubleLifeTank
    #   module works properly.
    def test_doublelifetank_getbulletproof(self):
        resolution = 630, 630
        pygame.display.set_mode(resolution)
        tank = doubleLifeTank(CoordinateT(8, 24))
        tank.bulletProof = True
        self.assertEqual(tank.getBulletProof(), True, "test_bulletproof_start")
        tank.bulletProof = False
        self.assertEqual(tank.getBulletProof(), False, "test_bulletproof_start"
                         )
        pygame.quit()


# Run the tests
if __name__ == '__main__':
    unittest.main()
