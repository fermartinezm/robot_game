import unittest
from mock import patch

from robot.src.exceptions.action_exception import ActionException
from robot.src.exceptions.args_exception import ArgsException
from robot.src.exceptions.faced_exception import FacedException
from robot.src.exceptions.limit_exception import LimitException
from robot.src.main.inputs import Inputs


class TestInputs(unittest.TestCase):

    def setUp(self):
        self.__INPUTS = {'inp': 'PLACE 0,0,NORTH'}
        self.robot = Inputs()

    def tearDown(self):
        """Override tearDown."""
        pass

    def test_01_check_north_point(self):
        print('Unit test :: Inputs :: Test 01 :: Check if NORTH is a valid '
              'cardinal point')
        error = 'Unit test :: Inputs :: Test 01 :: Failed'
        point = 'NORTH'
        result = self.robot.check_faced(point)
        self.assertEqual(result, point, error)

    def test_02_check_east_point(self):
        print('Unit test :: Inputs :: Test 02 :: Check if EAST is a valid '
              'cardinal point')
        error = 'Unit test :: Inputs :: Test 02 :: Failed'
        point = 'EAST'
        result = self.robot.check_faced(point)
        self.assertEqual(result, point, error)

    def test_03_check_south_point(self):
        print('Unit test :: Inputs :: Test 03 :: Check if SOUTH is a valid '
              'cardinal point')
        error = 'Unit test :: Inputs :: Test 03 :: Failed'
        point = 'SOUTH'
        result = self.robot.check_faced(point)
        self.assertEqual(result, point, error)

    def test_04_check_west_point(self):
        print('Unit test :: Inputs :: Test 04 :: Check if WEST is a valid '
              'cardinal point')
        error = 'Unit test :: Inputs :: Test 04 :: Failed'
        point = 'WEST'
        result = self.robot.check_faced(point)
        self.assertEqual(result, point, error)

    def test_05_check_non_existing_point(self):
        print('Unit test :: Inputs :: Test 05 :: Check a non existing '
              'cardinal point')
        point = 'SASDAFAF'
        with self.assertRaises(FacedException):
            self.robot.check_faced(point)

    def test_06_check_place_action(self):
        print('Unit test :: Inputs :: Test 06 :: Check if PLACE is a valid '
              'action')
        error = 'Unit test :: Inputs :: Test 06 :: Failed'
        action = 'PLACE'
        result = self.robot.check_action(action)
        self.assertEqual(result, action, error)

    def test_07_check_move_action(self):
        print('Unit test :: Inputs :: Test 07 :: Check if MOVE is a valid '
              'action')
        error = 'Unit test :: Inputs :: Test 07 :: Failed'
        action = 'MOVE'
        result = self.robot.check_action(action)
        self.assertEqual(result, action, error)

    def test_08_check_right_action(self):
        print('Unit test :: Inputs :: Test 08 :: Check if RIGHT is a valid '
              'action')
        error = 'Unit test :: Inputs :: Test 08 :: Failed'
        action = 'RIGHT'
        result = self.robot.check_action(action)
        self.assertEqual(result, action, error)

    def test_09_check_left_action(self):
        print('Unit test :: Inputs :: Test 09 :: Check if LEFT is a valid '
              'action')
        error = 'Unit test :: Inputs :: Test 09 :: Failed'
        action = 'LEFT'
        result = self.robot.check_action(action)
        self.assertEqual(result, action, error)

    def test_10_check_report_action(self):
        print('Unit test :: Inputs :: Test 10 :: Check if REPORT is a valid '
              'action')
        error = 'Unit test :: Inputs :: Test 10 :: Failed'
        action = 'REPORT'
        result = self.robot.check_action(action)
        self.assertEqual(result, action, error)

    def test_11_check_non_existing_action(self):
        print('Unit test :: Inputs :: Test 11 :: Check a non existing action')
        action = 'ASDASDAS'
        with self.assertRaises(ActionException):
            self.robot.check_action(action)

    def test_12_check_0_position(self):
        print('Unit test :: Inputs :: Test 12 :: Check if 0 is a valid '
              'position')
        error = 'Unit test :: Inputs :: Test 12 :: Failed'
        limit = 0
        result = self.robot.check_limits(limit)
        self.assertEqual(result, limit, error)

    def test_13_check_1_position(self):
        print('Unit test :: Inputs :: Test 13 :: Check if 1 is a valid '
              'position')
        error = 'Unit test :: Inputs :: Test 13 :: Failed'
        limit = 1
        result = self.robot.check_limits(limit)
        self.assertEqual(result, limit, error)

    def test_14_check_2_position(self):
        print('Unit test :: Inputs :: Test 14 :: Check if 2 is a valid '
              'position')
        error = 'Unit test :: Inputs :: Test 14 :: Failed'
        limit = 2
        result = self.robot.check_limits(limit)
        self.assertEqual(result, limit, error)

    def test_15_check_3_position(self):
        print('Unit test :: Inputs :: Test 15 :: Check if 3 is a valid '
              'position')
        error = 'Unit test :: Inputs :: Test 15 :: Failed'
        limit = 3
        result = self.robot.check_limits(limit)
        self.assertEqual(result, limit, error)

    def test_16_check_4_position(self):
        print('Unit test :: Inputs :: Test 16 :: Check if 4 is a valid '
              'position')
        error = 'Unit test :: Inputs :: Test 16 :: Failed'
        limit = 4
        result = self.robot.check_limits(limit)
        self.assertEqual(result, limit, error)

    def test_17_check_position_below_limit(self):
        print('Unit test :: Inputs :: Test 17 :: Check if one position below '
              'the limit is accepted')
        limit = -1
        with self.assertRaises(LimitException):
            self.robot.check_limits(limit)

    def test_18_check_position_above_limit(self):
        print('Unit test :: Inputs :: Test 18 :: Check if one position above '
              'the limit is accepted')
        limit = 5
        with self.assertRaises(LimitException):
            self.robot.check_limits(limit)

    @patch('robot.src.main.inputs.Inputs.check_limits')
    @patch('robot.src.main.inputs.Inputs.check_faced')
    def test_19_check_args_taken(self, faced, limits):
        print('Unit test :: Inputs :: Test 19 :: Check if the arguments are '
              'being taken right')
        error = 'Unit test :: Inputs :: Test 19 :: Failed'
        faced.return_value = 'NORTH'
        limits.return_value = 0
        result = self.robot.get_place_arguments(self.__INPUTS)
        out = (0, 0, 'NORTH')
        self.assertEqual(result, out, error)

    @patch('robot.src.main.inputs.Inputs.check_action')
    @patch('robot.src.main.inputs.Inputs.get_place_arguments')
    def test_20_check_place_with_args(self, args, action):
        print('Unit test :: Inputs :: Test 20 :: Check if PLACE action with '
              'arguments is accepted')
        error = 'Unit test :: Inputs :: Test 20 :: Failed'
        args.return_value = (0, 0, 'NORTH')
        action.return_value = 'PLACE'
        out = {'cmd': 'PLACE', 'x': 0, 'y': 0, 'f': 'NORTH'}
        result = self.robot.treat_inputs(self.__INPUTS)
        self.assertEqual(result, out, error)

    @patch('robot.src.main.inputs.Inputs.check_action')
    @patch('robot.src.main.inputs.Inputs.get_place_arguments')
    def test_21_check_move_with_args(self, args, action):
        print('Unit test :: Inputs :: Test 21 :: Check if MOVE action with '
              'arguments is accepted')
        args.return_value = (0, 0, 'NORTH')
        action.return_value = 'MOVE'
        self.__INPUTS = {'inp': 'MOVE 0,0,NORTH'}
        with self.assertRaises(ArgsException):
            self.robot.treat_inputs(self.__INPUTS)


if __name__ == "__main__":
    unittest.main()
