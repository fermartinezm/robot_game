import unittest

from robot.src.main.placement import Placement


class TestMovement(unittest.TestCase):

    def setUp(self):
        self.__CURRENT_POS = {'x': None, 'y': None, 'f': None}
        self.__COMMAND = {'cmd': 'PLACE', 'x': 0, 'y': 0, 'f': 'NORTH'}
        self.robot = Placement()

    def tearDown(self):
        """Override tearDown."""
        pass

    def test_01_place_robot_most_southwest_point_facing_north(self):
        print('Unit test :: Placement :: Test 01 :: Place robot on the most '
              'southwest point, facing North. x=0, y=0, f=NORTH')
        error = 'Unit test :: Placement :: Test 01 :: Failed'
        result = self.robot.place(self.__COMMAND)
        self.assertEqual(result, {'x': 0, 'y': 0, 'f': 'NORTH'}, error)

    def test_02_place_robot_most_northeast_point_facing_south(self):
        print('Unit test :: Placement :: Test 02 :: Place robot on the most '
              'northeast point, facing South. x=4, y=4, f=SOUTH')
        error = 'Unit test :: Placement :: Test 02 :: Failed'
        self.__COMMAND = {'cmd': 'PLACE', 'x': 4, 'y': 4, 'f': 'SOUTH'}
        result = self.robot.place(self.__COMMAND)
        self.assertEqual(result, {'x': 4, 'y': 4, 'f': 'SOUTH'}, error)

    def test_03_place_robot_most_southeast_point_facing_west(self):
        print('Unit test :: Placement :: Test 03 :: Place robot on the most '
              'southeast point, facing West. x=4, y=1, f=WEST')
        error = 'Unit test :: Placement :: Test 03 :: Failed'
        self.__COMMAND = {'cmd': 'PLACE', 'x': 4, 'y': 0, 'f': 'WEST'}
        result = self.robot.place(self.__COMMAND)
        self.assertEqual(result, {'x': 4, 'y': 0, 'f': 'WEST'}, error)

    def test_04_place_robot_most_northwest_point_facing_east(self):
        print('Unit test :: Placement :: Test 04 :: Place robot on the most '
              'northwest point, facing East. x=1, y=4, f=EAST')
        error = 'Unit test :: Placement :: Test 04 :: Failed'
        self.__COMMAND = {'cmd': 'PLACE', 'x': 0, 'y': 4, 'f': 'EAST'}
        result = self.robot.place(self.__COMMAND)
        self.assertEqual(result, {'x': 0, 'y': 4, 'f': 'EAST'}, error)


if __name__ == "__main__":
    unittest.main()
