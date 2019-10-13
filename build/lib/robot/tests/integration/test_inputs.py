import unittest

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

    def test_01_right_input(self):
        print('Integration test :: Inputs :: Test 01 :: '
              'Check get_place_arguments method: Correct action '
              'and correct arguments. Input = PLACE 0,0,NORTH')
        error = 'Unit test :: Inputs :: Test 01 :: Failed'
        result = self.robot.get_place_arguments(self.__INPUTS)
        self.assertEqual(result, (0, 0, 'NORTH'), error)

    def test_02_wrong_args_format(self):
        print('Integration test :: Inputs :: Test 02 :: '
              'Check get_place_arguments method: Correct action '
              'and wrong args format. Input = PLACE 0.0.NORTH')
        self.__INPUTS = {'inp': 'PLACE 0.0.NORTH'}
        with self.assertRaises(Exception):
            self.robot.get_place_arguments(self.__INPUTS)

    def test_03_wrong_cardinal_point(self):
        print('Integration test :: Inputs :: Test 03 :: '
              'Check get_place_arguments method: Correct action '
              'and wrong cardinal point. Input = PLACE 0,0,ASDF')
        self.__INPUTS = {'inp': 'PLACE 0,0,ASDF'}
        with self.assertRaises(FacedException):
            self.robot.get_place_arguments(self.__INPUTS)

    def test_04_wrong_Y_positon(self):
        print('Integration test :: Inputs :: Test 04 :: '
              'Check get_place_arguments method: Correct action '
              'and wrong Y position, out of the North limit. '
              'Input = PLACE 0.5.NORTH')
        self.__INPUTS = {'inp': 'PLACE 0,5,NORTH'}
        with self.assertRaises(LimitException):
            self.robot.get_place_arguments(self.__INPUTS)

    def test_05_wrong_Y_position(self):
        print('Integration test :: Inputs :: Test 05 :: '
              'Check get_place_arguments method: Correct action '
              'and wrong Y position, out of the South limit. '
              'Input = PLACE 0.-1.NORTH')
        self.__INPUTS = {'inp': 'PLACE 0,-1,NORTH'}
        with self.assertRaises(LimitException):
            self.robot.get_place_arguments(self.__INPUTS)

    def test_06_wrong_X_position(self):
        print('Integration test :: Inputs :: Test 06 :: '
              'Check get_place_arguments method: Correct action '
              'and wrong X position, out of the East limit. '
              'Input = PLACE 5,0,NORTH')
        self.__INPUTS = {'inp': 'PLACE 5,0,NORTH'}
        with self.assertRaises(LimitException):
            self.robot.get_place_arguments(self.__INPUTS)

    def test_07_wrong_X_position(self):
        print('Integration test :: Inputs :: Test 07 :: '
              'Check get_place_arguments method: Correct action '
              'and wrong X position, out of the West limit. '
              'Input = PLACE -1,0,NORTH')
        self.__INPUTS = {'inp': 'PLACE -1,0,NORTH'}
        with self.assertRaises(LimitException):
            self.robot.get_place_arguments(self.__INPUTS)

    def test_08_place_action_no_args(self):
        print('Integration test :: Inputs :: Test 08 :: '
              'Check get_place_arguments method: PLACE action'
              ' without arguments. Input = PLACE')
        self.__INPUTS = {'inp': 'PLACE '}
        with self.assertRaises(Exception):
            self.robot.get_place_arguments(self.__INPUTS)

    def test_09_wrong_args_data_type(self):
        print('Integration test :: Inputs :: Test 09 :: '
              'Check get_place_arguments method: '
              'Wrong arguments data type. Input = PLACE asd,asd,asd')
        self.__INPUTS = {'inp': 'PLACE asd,asd,asd'}
        with self.assertRaises(Exception):
            self.robot.get_place_arguments(self.__INPUTS)

    def test_10_wrong_args_data_type(self):
        print('Integration test :: Inputs :: Test 10 :: '
              'Check get_place_arguments method: '
              'Wrong arguments data type. Input = PLACE *!*,*!*,asd')
        self.__INPUTS = {'inp': 'PLACE *!*,*!*,asd'}
        with self.assertRaises(Exception):
            self.robot.get_place_arguments(self.__INPUTS)

    def test_11_right_input(self):
        print('Integration test :: Inputs :: Test 11 :: '
              'Check treat_inputs method: Correct action '
              'and correct arguments. Input = PLACE 0,0,NORTH')
        error = 'Unit test :: Inputs :: Test 11 :: Failed'
        result = self.robot.treat_inputs(self.__INPUTS)
        output = {'cmd': 'PLACE', 'x': 0, 'y': 0, 'f': 'NORTH'}
        self.assertEqual(result, output, error)

    def test_12_wrong_args_format(self):
        print('Integration test :: Inputs :: Test 12 :: '
              'Check treat_inputs method: Correct action '
              'and wrong args format. Input = PLACE 0.0.NORTH')
        self.__INPUTS = {'inp': 'PLACE 0.0.NORTH'}
        with self.assertRaises(Exception):
            self.robot.treat_inputs(self.__INPUTS)

    def test_13_wrong_cardinal_point(self):
        print('Integration test :: Inputs :: Test 13 :: '
              'Check treat_inputs method: Correct action '
              'and wrong cardinal point. Input = PLACE 0,0,ASDF')
        self.__INPUTS = {'inp': 'PLACE 0,0,ASDF'}
        with self.assertRaises(FacedException):
            self.robot.treat_inputs(self.__INPUTS)

    def test_14_wrong_Y_positon(self):
        print('Integration test :: Inputs :: Test 14 :: '
              'Check treat_inputs method: Correct action '
              'and wrong Y position, out of the North limit. '
              'Input = PLACE 0.5.NORTH')
        self.__INPUTS = {'inp': 'PLACE 0,5,NORTH'}
        with self.assertRaises(LimitException):
            self.robot.treat_inputs(self.__INPUTS)

    def test_15_wrong_Y_position(self):
        print('Integration test :: Inputs :: Test 15 :: '
              'Check treat_inputs method: Correct action '
              'and wrong Y position, out of the South limit. '
              'Input = PLACE 0.-1.NORTH')
        self.__INPUTS = {'inp': 'PLACE 0,-1,NORTH'}
        with self.assertRaises(LimitException):
            self.robot.treat_inputs(self.__INPUTS)

    def test_16_wrong_X_position(self):
        print('Integration test :: Inputs :: Test 16 :: '
              'Check treat_inputs method: Correct action '
              'and wrong X position, out of the East limit. '
              'Input = PLACE 5,0,NORTH')
        self.__INPUTS = {'inp': 'PLACE 5,0,NORTH'}
        with self.assertRaises(LimitException):
            self.robot.treat_inputs(self.__INPUTS)

    def test_17_wrong_X_position(self):
        print('Integration test :: Inputs :: Test 17 :: '
              'Check treat_inputs method: Correct action '
              'and wrong X position, out of the West limit. '
              'Input = PLACE -1,0,NORTH')
        self.__INPUTS = {'inp': 'PLACE -1,0,NORTH'}
        with self.assertRaises(LimitException):
            self.robot.treat_inputs(self.__INPUTS)

    def test_18_place_action_no_args(self):
        print('Integration test :: Inputs :: Test 18 :: '
              'Check treat_inputs method: PLACE action'
              ' without arguments. Input = PLACE')
        self.__INPUTS = {'inp': 'PLACE '}
        with self.assertRaises(Exception):
            self.robot.treat_inputs(self.__INPUTS)

    def test_19_wrong_args_data_type(self):
        print('Integration test :: Inputs :: Test 19 :: '
              'Check treat_inputs method: '
              'Wrong arguments data type. Input = PLACE asd,asd,asd')
        self.__INPUTS = {'inp': 'PLACE asd,asd,asd'}
        with self.assertRaises(Exception):
            self.robot.treat_inputs(self.__INPUTS)

    def test_20_move_action_no_args(self):
        print('Integration test :: Inputs :: Test 20 :: '
              'Check treat_inputs method: '
              'MOVE action without arguments. Input = MOVE')
        self.__INPUTS = {'inp': 'MOVE'}
        error = 'Unit test :: Inputs :: Test 21 :: Failed'
        result = self.robot.treat_inputs(self.__INPUTS)
        output = {'cmd': 'MOVE'}
        self.assertEqual(result, output, error)

    def test_21_report_action_no_args(self):
        print('Integration test :: Inputs :: Test 22 :: '
              'Check treat_inputs method: '
              'REPORT action without arguments. Input = REPORT')
        self.__INPUTS = {'inp': 'REPORT'}
        error = 'Unit test :: Inputs :: Test 22 :: Failed'
        result = self.robot.treat_inputs(self.__INPUTS)
        output = {'cmd': 'REPORT'}
        self.assertEqual(result, output, error)

    def test_22_left_action_no_args(self):
        print('Integration test :: Inputs :: Test 22 :: '
              'Check treat_inputs method: '
              'LEFT action without arguments. Input = LEFT')
        self.__INPUTS = {'inp': 'LEFT'}
        error = 'Unit test :: Inputs :: Test 23 :: Failed'
        result = self.robot.treat_inputs(self.__INPUTS)
        output = {'cmd': 'LEFT'}
        self.assertEqual(result, output, error)

    def test_23_rigth_action_no_args(self):
        print('Integration test :: Inputs :: Test 23 :: '
              'Check treat_inputs method: '
              'RIGHT action without arguments. Input = RIGHT')
        self.__INPUTS = {'inp': 'RIGHT'}
        error = 'Unit test :: Inputs :: Test 23 :: Failed'
        result = self.robot.treat_inputs(self.__INPUTS)
        output = {'cmd': 'RIGHT'}
        self.assertEqual(result, output, error)

    def test_24_non_existing_action(self):
        print('Integration test :: Inputs :: Test 24 :: '
              'Check treat_inputs method: '
              'ASD action without arguments. Input = ASD')
        self.__INPUTS = {'inp': 'ASD'}
        with self.assertRaises(ActionException):
            self.robot.treat_inputs(self.__INPUTS)

    def test_25_non_existing_action(self):
        print('Integration test :: Inputs :: Test 25 :: '
              'Check treat_inputs method: '
              '123 action without arguments. Input = 123')
        self.__INPUTS = {'inp': '123'}
        with self.assertRaises(ActionException):
            self.robot.treat_inputs(self.__INPUTS)

    def test_26_rigth_action_with_args(self):
        print('Integration test :: Inputs :: Test 26 :: '
              'Check treat_inputs method: '
              'RIGHT action with arguments. Input = RIGHT 0,0,NORTH')
        self.__INPUTS = {'inp': 'RIGHT 0,0,NORTH'}
        with self.assertRaises(ArgsException):
            self.robot.treat_inputs(self.__INPUTS)

    def test_27_move_action_with_args(self):
        print('Integration test :: Inputs :: Test 27 :: '
              'Check treat_inputs method: '
              'MOVE action with arguments. Input = MOVE 0,0,NORTH')
        self.__INPUTS = {'inp': 'MOVE 0,0,NORTH'}
        with self.assertRaises(ArgsException):
            self.robot.treat_inputs(self.__INPUTS)


if __name__ == "__main__":
    unittest.main()
