import unittest

from robot.src.exceptions.fall_exception import FallException
from robot.src.main.movement import Movement


class TestMovement(unittest.TestCase):

    def setUp(self):
        self.__CURRENT_POS = {'x': 2, 'y': 2, 'f': 'NORTH'}
        self.robot = Movement()

    def tearDown(self):
        """Override tearDown."""
        pass

    def test_01_move_north(self):
        print('Unit test :: Movement :: Test 01 :: Move robot to NORTH')
        error = 'Unit test :: Movement :: Test 01 :: Failed'
        result = self.robot.move(self.__CURRENT_POS)
        self.assertEqual(result['y'], 3, error)

    def test_02_move_west(self):
        print('Unit test :: Movement :: Test 02 :: Move robot to WEST')
        error = 'Unit test :: Movement :: Test 02 :: Failed'
        self.__CURRENT_POS['f'] = 'WEST'
        result = self.robot.move(self.__CURRENT_POS)
        self.assertEqual(result['x'], 1, error)

    def test_03_move_south(self):
        print('Unit test :: Movement :: Test 03 :: Move robot to SOUTH')
        error = 'Unit test :: Movement :: Test 03 :: Failed'
        self.__CURRENT_POS['f'] = 'SOUTH'
        result = self.robot.move(self.__CURRENT_POS)
        self.assertEqual(result['y'], 1, error)

    def test_04_move_east(self):
        print('Unit test :: Movement :: Test 04 :: Move robot to EAST')
        error = 'Unit test :: Movement :: Test 04 :: Failed'
        self.__CURRENT_POS['f'] = 'EAST'
        result = self.robot.move(self.__CURRENT_POS)
        self.assertEqual(result['x'], 3, error)

    def test_05_move_north_not_fall(self):
        print('Unit test :: Movement :: Test 05 :: '
              'Check robot does not fall when moving to NORTH')
        self.__CURRENT_POS['y'] = 4
        with self.assertRaises(FallException):
            self.robot.move(self.__CURRENT_POS)

    def test_06_move_west_not_fall(self):
        print('Unit test :: Movement :: Test 06 :: '
              'Check robot does not fall when moving to WEST')
        self.__CURRENT_POS['f'] = 'WEST'
        self.__CURRENT_POS['x'] = 0
        with self.assertRaises(FallException):
            self.robot.move(self.__CURRENT_POS)

    def test_07_move_south_not_fall(self):
        print('Unit test :: Movement :: Test 07 :: '
              'Check robot does not fall when moving to SOUTH')
        self.__CURRENT_POS['f'] = 'SOUTH'
        self.__CURRENT_POS['y'] = 0
        with self.assertRaises(FallException):
            self.robot.move(self.__CURRENT_POS)

    def test_08_move_east_not_fall(self):
        print('Unit test :: Movement :: Test 08 :: '
              'Check robot does not fall when moving to EAST')
        self.__CURRENT_POS['f'] = 'EAST'
        self.__CURRENT_POS['x'] = 4
        with self.assertRaises(FallException):
            self.robot.move(self.__CURRENT_POS)


if __name__ == "__main__":
    unittest.main()
