import unittest
from mock import patch

from robot.src.exceptions.limit_exception import LimitException
from robot.src.main.orchestrator import Orchestrator


class TestInOut(unittest.TestCase):

    def setUp(self):
        self.__CURRENT_POS = {'x': 1, 'y': 1, 'f': 'SOUTH'}
        self.__COMMAND = {'cmd': 'PLACE', 'x': 0, 'y': 0, 'f': 'NORTH'}
        self.robot = Orchestrator()

    def tearDown(self):
        """Override tearDown."""
        pass

    @patch('robot.src.main.placement.Placement.place')
    def test_01_place_action(self, place):
        print('Integration test :: Orchestrator :: Test 01 :: Check if PLACE '
              'action is executed')
        error = 'Unit test :: Orchestrator :: Test 01 :: Failed'
        place.return_value = {'x': 0, 'y': 0, 'f': 'NORTH'}
        out = {'x': 0, 'y': 0, 'f': 'NORTH'}
        result = self.robot.execute_command(
            self.__COMMAND, self.__CURRENT_POS)
        self.assertEqual(result, out, error)

    @patch('robot.src.main.movement.Movement.move')
    def test_02_move_action(self, move):
        print('Integration test :: Orchestrator :: Test 02 :: Check if MOVE action is '
              'executed')
        error = 'Unit test :: Orchestrator :: Test 02 :: Failed'
        self.__COMMAND = {'cmd': 'MOVE'}
        move.return_value = {'x': 0, 'y': 1, 'f': 'NORTH'}
        out = {'x': 0, 'y': 1, 'f': 'NORTH'}
        result = self.robot.execute_command(
            self.__COMMAND, self.__CURRENT_POS)
        self.assertEqual(result, out, error)

    @patch('robot.src.main.rotation.Rotation.rotate')
    def test_03_right_action(self, rotate):
        print('Integration test :: Orchestrator :: Test 03 :: Check if RIGHT '
              'action is executed')
        error = 'Unit test :: Orchestrator :: Test 03 :: Failed'
        self.__COMMAND = {'cmd': 'RIGHT'}
        rotate.return_value = {'x': 0, 'y': 1, 'f': 'EAST'}
        out = {'x': 0, 'y': 1, 'f': 'EAST'}
        result = self.robot.execute_command(
            self.__COMMAND, self.__CURRENT_POS)
        self.assertEqual(result, out, error)

    @patch('robot.src.main.rotation.Rotation.rotate')
    def test_04_left_action(self, rotate):
        print('Integration test :: Orchestrator :: Test 04 :: Check if LEFT '
              'action is executed')
        error = 'Unit test :: Orchestrator :: Test 04 :: Failed'
        self.__COMMAND = {'cmd': 'LEFT'}
        rotate.return_value = {'x': 0, 'y': 1, 'f': 'WEST'}
        out = {'x': 0, 'y': 1, 'f': 'WEST'}
        result = self.robot.execute_command(
            self.__COMMAND, self.__CURRENT_POS)
        self.assertEqual(result, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    @patch('robot.src.main.inputs.Inputs.treat_inputs')
    def test_05_start_game(self, inputs, keyboard):
        print('Unit test :: Orchestrator :: Test 05 :: Start the game '
              'placing the robot')
        error = 'Unit test :: Orchestrator :: Test 05 :: Failed'
        self.__CURRENT_POS = {'x': None, 'y': None, 'f': None}
        keyboard.return_value = 'PLACE 0,0,NORTH'
        inputs.return_value = {'cmd': 'PLACE', 'x': 0, 'y': 0, 'f': 'NORTH'}
        start = 0
        result = self.robot.run_game(self.__CURRENT_POS, start)
        out = {'x': 0, 'y': 0, 'f': 'NORTH'}, 1
        self.assertEqual(result, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    @patch('robot.src.main.orchestrator.Orchestrator.treat_inputs')
    def test_06_place_robot_game_started(self, inputs, keyboard):
        print('Unit test :: Orchestrator :: Test 06 :: Place the robot when  '
              'the game is already started')
        error = 'Unit test :: Orchestrator :: Test 06 :: Failed'
        self.__CURRENT_POS = {'x': 0, 'y': 0, 'f': 'SOUTH'}
        keyboard.return_value = 'PLACE 4,4,NORTH'
        inputs.return_value = {'cmd': 'PLACE', 'x': 4, 'y': 4, 'f': 'NORTH'}
        start = 1
        result = self.robot.run_game(self.__CURRENT_POS, start)
        out = {'x': 4, 'y': 4, 'f': 'NORTH'}, 1
        self.assertEqual(result, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    @patch('robot.src.main.orchestrator.Orchestrator.treat_inputs')
    def test_07_right_game_not_started(self, inputs, keyboard):
        print('Unit test :: Orchestrator :: Test 07 :: RIGHT action when '
              'is not started')
        error = 'Unit test :: Orchestrator :: Test 07 :: Failed'
        self.__CURRENT_POS = {'x': None, 'y': None, 'f': None}
        keyboard.return_value = 'RIGHT'
        inputs.return_value = {'cmd': 'RIGHT'}
        start = 0
        result = self.robot.run_game(self.__CURRENT_POS, start)
        out = {'x': None, 'y': None, 'f': None}, 0
        self.assertEqual(result, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    @patch('robot.src.main.orchestrator.Orchestrator.treat_inputs',
           side_effect=Exception(LimitException))
    def test_08_place_position_above_limit(self, inputs, keyboard):
        print('Unit test :: Orchestrator :: Test 08 :: PLACE action when '
              'the position is above the limit')
        error = 'Unit test :: Orchestrator :: Test 08 :: Failed'
        self.__CURRENT_POS = {'x': None, 'y': None, 'f': None}
        keyboard.return_value = 'PLACE 5,0,NORTH'
        start = 0
        result = self.robot.run_game(self.__CURRENT_POS, start)
        out = {'x': None, 'y': None, 'f': None}, 0
        self.assertEqual(result, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    @patch('robot.src.main.orchestrator.Orchestrator.treat_inputs')
    def test_09_move_game_started(self, inputs, keyboard):
        print('Unit test :: Orchestrator :: Test 09 :: Check MOVE action'
              ' when the robot is placed')
        error = 'Unit test :: Orchestrator :: Test 09 :: Failed'
        self.__CURRENT_POS = {'x': 0, 'y': 0, 'f': 'NORTH'}
        keyboard.return_value = 'MOVE'
        inputs.return_value = {'cmd': 'MOVE'}
        start = 1
        result = self.robot.run_game(self.__CURRENT_POS, start)
        out = {'x': 0, 'y': 1, 'f': 'NORTH'}, 1
        self.assertEqual(result, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    @patch('robot.src.main.orchestrator.Orchestrator.treat_inputs')
    def test_10_left_game_started(self, inputs, keyboard):
        print('Unit test :: Orchestrator :: Test 10 :: Check LEFT action'
              ' when the robot is placed')
        error = 'Unit test :: Orchestrator :: Test 10 :: Failed'
        self.__CURRENT_POS = {'x': 0, 'y': 0, 'f': 'NORTH'}
        keyboard.return_value = 'LEFT'
        inputs.return_value = {'cmd': 'LEFT'}
        start = 1
        result = self.robot.run_game(self.__CURRENT_POS, start)
        out = {'x': 0, 'y': 0, 'f': 'WEST'}, 1
        self.assertEqual(result, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    @patch('robot.src.main.orchestrator.Orchestrator.treat_inputs')
    def test_11_right_game_started(self, inputs, keyboard):
        print('Unit test :: Orchestrator :: Test 11 :: Check RIGHT action'
              ' when the robot is placed')
        error = 'Unit test :: Orchestrator :: Test 11 :: Failed'
        self.__CURRENT_POS = {'x': 0, 'y': 0, 'f': 'NORTH'}
        keyboard.return_value = 'RIGHT'
        inputs.return_value = {'cmd': 'RIGHT'}
        start = 1
        result = self.robot.run_game(self.__CURRENT_POS, start)
        out = {'x': 0, 'y': 0, 'f': 'EAST'}, 1
        self.assertEqual(result, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    @patch('robot.src.main.orchestrator.Orchestrator.treat_inputs')
    def test_10_report_game_started(self, inputs, keyboard):
        print('Unit test :: Orchestrator :: Test 12 :: Check REPORT action'
              ' when the robot is placed')
        error = 'Unit test :: Orchestrator :: Test 12 :: Failed'
        self.__CURRENT_POS = {'x': 0, 'y': 0, 'f': 'NORTH'}
        keyboard.return_value = 'REPORT'
        inputs.return_value = {'cmd': 'REPORT'}
        start = 1
        result = self.robot.run_game(self.__CURRENT_POS, start)
        out = {'x': 0, 'y': 0, 'f': 'NORTH'}, 1
        self.assertEqual(result, out, error)


if __name__ == "__main__":
    unittest.main()
