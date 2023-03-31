## @file mapSavingTest.py
#  @author Xinyu Huang, Di Wu, Jiahao Zhou
#  @brief Map Saving Test Module
#  @date 04/04/2020

import sys
import unittest
sys.path.append("../src")
from Map import Map, PVPMap, PVEMap


## @brief Unit test for the verification of the saved Map.
#  @detail This class do the unit test cases to compare the saved map file
#  with the expected map file, and it passes once the contents in these
#  two file are equivalent.
class MapSavingTest(unittest.TestCase):

    ## @brief Test if the saved map file are the same as the one expected.
    def test_savemap_verification(self):
        testMap = Map()
        testMap.loadBrickIron("../map/PVEMap/Map1(default)")
        testMap.saveMap("../testMap")
        f1 = open("testMap", "r")
        f2 = open("../map/PVEMap/Map1(default)", "r")
        self.assertEqual(f1.read(), f2.read())
        f1.close()
        f2.close()

    ## @brief Test if the add brick function is available.
    def map_add_test1(self):
        testMap = Map()
        coordinateT1 = CoordinateT(8, 8)
        testMap.addBrick(coordinateT1)
        x = 3 + 8 * 24
        y = 3 + 8 * 24
        for i in testMap.brickGroup:
            self.assertEqual(i.rect.left, x)
            self.assertEqual(i.rect.top, y)

    ## @brief Test if the add iron function is available.
    def map_add_test2(self):
        testMap = Map()
        coordinateT1 = CoordinateT(8, 8)
        testMap.addIron(coordinateT1)
        x = 3 + 8 * 24
        y = 3 + 8 * 24
        for i in testMap.ironGroup:
            self.assertEqual(i.rect.left, x)
            self.assertEqual(i.rect.top, y)



# Run the tests
if __name__ == '__main__':
    unittest.main()
