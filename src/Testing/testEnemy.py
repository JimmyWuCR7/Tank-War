## @file enemyTankTest.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief Enemy Tank Test Module
#  @date 04/04/2020

import sys
sys.path.append("../src")
import unittest
import pygame
from enemyTank import EnemyTank


## @brief Unit test for enemyTank Module.
#  @detail This class do the unit test cases for part of the functions in
#  the enemyTank Module, and it passes once all the outputs are the same
#  as the expected ones.
class EnemyTankTest(unittest.TestCase):

    ## @brief Test if the shoot function in enemyTank module works
    #  properly.
    def test_enemytank_shoot(self):
        resolution = 630, 630
        pygame.display.set_mode(resolution)
        enemy = EnemyTank(None, None, None, 0)
        enemy.shoot()
        self.assertEqual(enemy.bullet.life, True, "test_enemytank_shoot")
        pygame.quit()


# Run the tests
if __name__ == '__main__':
    unittest.main()
