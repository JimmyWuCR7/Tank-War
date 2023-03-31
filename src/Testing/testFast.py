## @file fastBulletTankTest.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief Fast Bullet Tank Test Module
#  @date 04/04/2020

import sys
sys.path.append("../src")
import unittest
import pygame
from Map import CoordinateT
from fastBulletTank import fastBulletTank


## @brief Unit test for fastBulletTank module.
#  @detail This class do the unit test cases for part of the functions in
#  the fastBulletTank module, and it passes once all the outputs are the same
#  as the expected ones.
class fastBulletTankTest(unittest.TestCase):

    ## @brief Test if the doubleBullet function in fastBulletTank module
    #   works properly.
    def test_fastbullettank_doublebullet(self):
        resolution = 630, 630
        pygame.display.set_mode(resolution)
        tank = fastBulletTank(CoordinateT(8, 24))
        tank.level = 1
        tank.doubleBullet()
        self.assertEqual([tank.bullet.life, tank.bullet2.life,
                          tank.bullet.speed, tank.bullet2.speed,
                          tank.bullet.strong, tank.bullet2.strong],
                         [True, True, 20, 20, False, False],
                         "test_doublebullet")
        tank.level = 2
        tank.doubleBullet()
        self.assertEqual([tank.bullet.life, tank.bullet2.life,
                          tank.bullet.speed, tank.bullet2.speed,
                          tank.bullet.strong, tank.bullet2.strong],
                         [True, True, 20, 20, True, True],
                         "test_doublebullet")
        tank.level = 3
        tank.doubleBullet()
        self.assertEqual([tank.bullet.life, tank.bullet2.life,
                          tank.bullet.speed, tank.bullet2.speed,
                          tank.bullet.strong, tank.bullet2.strong],
                         [True, True, 48, 48, True, True],
                         "test_doublebullet")
        tank.dir_x, tank.dir_y = 0, -1
        tank.doubleBullet()
        self.assertEqual([tank.bullet.rect.left, tank.bullet.rect.bottom],
                         [tank.rect.left + 20, tank.rect.top + 1],
                         "test_doublebullet")
        tank.dir_x, tank.dir_y = 0, 1
        tank.doubleBullet()
        self.assertEqual([tank.bullet.rect.left, tank.bullet.rect.top],
                         [tank.rect.left + 20, tank.rect.bottom - 1],
                         "test_doublebullet")
        tank.dir_x, tank.dir_y = -1, 0
        tank.doubleBullet()
        self.assertEqual([tank.bullet.rect.right, tank.bullet.rect.top],
                         [tank.rect.left - 1, tank.rect.top + 20],
                         "test_doublebullet")
        tank.dir_x, tank.dir_y = 1, 0
        tank.doubleBullet()
        self.assertEqual([tank.bullet.rect.left, tank.bullet.rect.top],
                         [tank.rect.right + 1, tank.rect.top + 20],
                         "test_doublebullet")
        pygame.quit()


# Run the tests
if __name__ == '__main__':
    unittest.main()
