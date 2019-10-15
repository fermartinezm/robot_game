import unittest
from mock import patch

from robot.src.exceptions.limit_exception import LimitException
from robot.src.exceptions.start_exception import StartException
from robot.src.main.orchestrator import Orchestrator


class TestInOut(unittest.TestCase):

    def setUp(self):
        self.__CURRENT_POS = {'x': 1, 'y': 1, 'f': 'SOUTH'}
        self.__COMMAND = {'cmd': 'PLACE', 'x': 0, 'y': 0, 'f': 'NORTH'}
        self.robot = Orchestrator()

    def tearDown(self):
        """Override tearDown."""
        pass

    def my_side_effect(self):
        raise Exception("Test")

    @patch('robot.src.main.orchestrator.Orchestrator.place_robot')
    def test_01_place_action(self, place):
        print('Unit test :: Orchestrator :: Test 01 :: Check if PLACE '
              'action is executed')
        error = 'Unit test :: Orchestrator :: Test 01 :: Failed'
        place.return_value = {'x': 0, 'y': 0, 'f': 'NORTH'}
        out = {'x': 0, 'y': 0, 'f': 'NORTH'}
        result = self.robot.execute_command(
            self.__COMMAND, self.__CURRENT_POS)
        self.assertEqual(result, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.move_robot')
    def test_02_move_action(self, move):
        print('Unit test :: Orchestrator :: Test 02 :: Check if MOVE '
              'action is executed')
        error = 'Unit test :: Orchestrator :: Test 02 :: Failed'
        self.__COMMAND = {'cmd': 'MOVE'}
        move.return_value = {'x': 0, 'y': 1, 'f': 'NORTH'}
        out = {'x': 0, 'y': 1, 'f': 'NORTH'}
        result = self.robot.execute_command(
            self.__COMMAND, self.__CURRENT_POS)
        self.assertEqual(result, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.rotate_robot')
    def test_03_right_action(self, rotate):
        print('Unit test :: Orchestrator :: Test 03 :: Check if RIGHT '
              'action is executed')
        error = 'Unit test :: Orchestrator :: Test 03 :: Failed'
        self.__COMMAND = {'cmd': 'RIGHT'}
        rotate.return_value = {'x': 0, 'y': 1, 'f': 'EAST'}
        out = {'x': 0, 'y': 1, 'f': 'EAST'}
        result = self.robot.execute_command(
            self.__COMMAND, self.__CURRENT_POS)
        self.assertEqual(result, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.rotate_robot')
    def test_04_left_action(self, rotate):
        print('Unit test :: Orchestrator :: Test 04 :: Check if LEFT '
              'action is executed')
        error = 'Unit test :: Orchestrator :: Test 04 :: Failed'
        self.__COMMAND = {'cmd': 'LEFT'}
        rotate.return_value = {'x': 0, 'y': 1, 'f': 'WEST'}
        out = {'x': 0, 'y': 1, 'f': 'WEST'}
        result = self.robot.execute_command(
            self.__COMMAND, self.__CURRENT_POS)
        self.assertEqual(result, out, error)

    def test_05_report_action(self):
        print('Unit test :: Orchestrator :: Test 05 :: Check if REPORT '
              'action is executed')
        error = 'Unit test :: Orchestrator :: Test 05 :: Failed'
        self.__COMMAND = {'cmd': 'REPORT'}
        out = {'x': 1, 'y': 1, 'f': 'SOUTH'}
        result = self.robot.execute_command(
            self.__COMMAND, self.__CURRENT_POS)
        self.assertEqual(result, out, error)

    def test_06_check_state_robot_not_placed(self):
        print('Unit test :: Orchestrator :: Test 06 :: Do not realize the action '
              'when the robot is not still placed')
        self.__COMMAND = {'cmd': 'MOVE'}
        self.__CURRENT_POS = {'x': None, 'y': None, 'f': None}
        with self.assertRaises(StartException):
            self.robot.start(self.__COMMAND, self.__CURRENT_POS)

    def test_07_check_state_robot_placed(self):
        print('Unit test :: Orchestrator :: Test 07 :: Check robot is placed '
              'for first time')
        self.__CURRENT_POS = {'x': None, 'y': None, 'f': None}
        error = 'Unit test :: Orchestrator :: Test 07 :: Failed'
        result = self.robot.start(self.__COMMAND, self.__CURRENT_POS)
        self.assertEqual(result, 1, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    @patch('robot.src.main.orchestrator.Orchestrator.execute_command')
    @patch('robot.src.main.orchestrator.Orchestrator.treat_inputs')
    @patch('robot.src.main.orchestrator.Orchestrator.start')
    def test_08_start_game(self, start, inputs, cmd, keyboard):
        print('Unit test :: Orchestrator :: Test 08 :: Start the game '
              'placing the robot')
        error = 'Unit test :: Orchestrator :: Test 08 :: Failed'
        self.__CURRENT_POS = {'x': None, 'y': None, 'f': None}
        keyboard.return_value = 'PLACE 0,0,NORTH'
        inputs.return_value = {'cmd': 'PLACE', 'x': 0, 'y': 0, 'f': 'NORTH'}
        start.return_value = 1
        cmd.return_value = {'x': 0, 'y': 0, 'f': 'NORTH'}
        start = 0
        result = self.robot.run_game(self.__CURRENT_POS, start)
        out = {'x': 0, 'y': 0, 'f': 'NORTH'}, 1
        self.assertEqual(result, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    @patch('robot.src.main.orchestrator.Orchestrator.execute_command')
    @patch('robot.src.main.orchestrator.Orchestrator.treat_inputs')
    @patch('robot.src.main.orchestrator.Orchestrator.start')
    def test_09_place_robot_game_started(self, start, inputs, cmd, keyboard):
        print('Unit test :: Orchestrator :: Test 09 :: Place the robot when  '
              'the game is already started')
        error = 'Unit test :: Orchestrator :: Test 09 :: Failed'
        self.__CURRENT_POS = {'x': 0, 'y': 0, 'f': 'SOUTH'}
        keyboard.return_value = 'PLACE 4,4,NORTH'
        inputs.return_value = {'cmd': 'PLACE', 'x': 4, 'y': 4, 'f': 'NORTH'}
        start.return_value = 1
        cmd.return_value = {'x': 4, 'y': 4, 'f': 'NORTH'}
        start = 1
        result = self.robot.run_game(self.__CURRENT_POS, start)
        out = {'x': 4, 'y': 4, 'f': 'NORTH'}, 1
        self.assertEqual(result, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    @patch('robot.src.main.orchestrator.Orchestrator.execute_command')
    @patch('robot.src.main.orchestrator.Orchestrator.treat_inputs')
    @patch('robot.src.main.orchestrator.Orchestrator.start',
           side_effect=Exception(StartException))
    def test_10_right_game_not_started(self, start, inputs, cmd, keyboard):
        print('Unit test :: Orchestrator :: Test 10 :: RIGHT action when '
              'is not started')
        error = 'Unit test :: Orchestrator :: Test 10 :: Failed'
        self.__CURRENT_POS = {'x': None, 'y': None, 'f': None}
        keyboard.return_value = 'RIGHT'
        inputs.return_value = {'cmd': 'RIGHT'}
        cmd.return_value = {'cmd': 'RIGHT'}
        start = 0
        result = self.robot.run_game(self.__CURRENT_POS, start)
        out = {'x': None, 'y': None, 'f': None}, 0
        self.assertEqual(result, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    @patch('robot.src.main.orchestrator.Orchestrator.execute_command')
    @patch('robot.src.main.orchestrator.Orchestrator.treat_inputs',
           side_effect=Exception(LimitException))
    @patch('robot.src.main.orchestrator.Orchestrator.start')
    def test_11_place_position_above_limit(
            self, start, inputs, cmd, keyboard):
        print('Unit test :: Orchestrator :: Test 11 :: PLACE action when '
              'the position is above the limit')
        error = 'Unit test :: Orchestrator :: Test 11 :: Failed'
        self.__CURRENT_POS = {'x': None, 'y': None, 'f': None}
        keyboard.return_value = 'PLACE 5,0,NORTH'
        start.return_value = 1
        cmd.return_value = {'x': 0, 'y': 0, 'f': 'NORTH'}
        start = 0
        result = self.robot.run_game(self.__CURRENT_POS, start)
        out = {'x': None, 'y': None, 'f': None}, 0
        self.assertEqual(result, out, error)


if __name__ == "__main__":
    unittest.main()
