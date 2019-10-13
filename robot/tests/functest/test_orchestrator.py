import unittest
from mock import patch

from robot.src.exceptions.start_exception import StartException
from robot.src.main.orchestrator import Orchestrator


class TestOrchestrator(unittest.TestCase):

    def setUp(self):
        self.robot = Orchestrator()

    def tearDown(self):
        """Override tearDown."""
        pass

    def get_input(text):
        return input(text)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_01_move_action_not_placed_robot(self, keyboard):
        print('Functional test :: Orchestrator :: Test 01 :: Robot does not '
              'move when the robot is not still placed')
        error = 'Unit test :: Orchestrator :: Test 01 :: Failed'
        current_position = {'x': None, 'y': None, 'f': None}
        init = 0
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': None, 'y': None, 'f': None}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_02_right_action_not_placed_robot(self, keyboard):
        print('Functional test :: Orchestrator :: Test 02 :: Robot does not '
              'rotate to the right when the robot is not still placed')
        error = 'Unit test :: Orchestrator :: Test 02 :: Failed'
        current_position = {'x': None, 'y': None, 'f': None}
        init = 0
        keyboard.return_value = 'RIGHT'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': None, 'y': None, 'f': None}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_03_left_action_not_placed_robot(self, keyboard):
        print('Functional test :: Orchestrator :: Test 03 :: Robot does not '
              'rotate to the left when the robot is not still placed')
        error = 'Unit test :: Orchestrator :: Test 03 :: Failed'
        current_position = {'x': None, 'y': None, 'f': None}
        init = 0
        keyboard.return_value = 'LEFT'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': None, 'y': None, 'f': None}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_04_report_action_not_placed_robot(self, keyboard):
        print('Functional test :: Orchestrator :: Test 04 :: Robot does not '
              'report when the robot is not still placed')
        error = 'Unit test :: Orchestrator :: Test 04 :: Failed'
        current_position = {'x': None, 'y': None, 'f': None}
        init = 0
        keyboard.return_value = 'REPORT'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': None, 'y': None, 'f': None}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_05_place_robot(self, keyboard):
        print('Functional test :: Orchestrator :: Test 05 :: Check '
              'PLACE action')
        error = 'Unit test :: Orchestrator :: Test 05 :: Failed'
        current_position = {'x': None, 'y': None, 'f': None}
        init = 0
        keyboard.return_value = 'PLACE 0,0,NORTH'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 0, 'f': 'NORTH'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_06_move_robot(self, keyboard):
        print('Functional test :: Orchestrator :: Test 06 :: Check '
              'MOVE action when the robot has been placed')
        error = 'Unit test :: Orchestrator :: Test 06 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'NORTH'}
        init = 0
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 1, 'f': 'NORTH'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_07_right_robot(self, keyboard):
        print('Functional test :: Orchestrator :: Test 07 :: Check '
              'RIGHT action when the robot has been placed')
        error = 'Unit test :: Orchestrator :: Test 07 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'NORTH'}
        init = 0
        keyboard.return_value = 'RIGHT'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 0, 'f': 'EAST'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_08_left_robot(self, keyboard):
        print('Functional test :: Orchestrator :: Test 08 :: Check '
              'LEFT action when the robot has been placed')
        error = 'Unit test :: Orchestrator :: Test 08 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'NORTH'}
        init = 0
        keyboard.return_value = 'LEFT'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 0, 'f': 'WEST'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_09_report_robot(self, keyboard):
        print('Functional test :: Orchestrator :: Test 09 :: Check '
              'REPORT action when the robot has been placed')
        error = 'Unit test :: Orchestrator :: Test 09 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'NORTH'}
        init = 0
        keyboard.return_value = 'REPORT'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 0, 'f': 'NORTH'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_10_robot_not_fall_north(self, keyboard):
        print('Functional test :: Orchestrator :: Test 10 :: Check '
              'the robot does not fall from North edge')
        error = 'Unit test :: Orchestrator :: Test 10 :: Failed'
        current_position = {'x': 0, 'y': 4, 'f': 'NORTH'}
        init = 0
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 4, 'f': 'NORTH'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_11_robot_not_fall_north(self, keyboard):
        print('Functional test :: Orchestrator :: Test 11 :: Check '
              'the robot does not fall from South edge')
        error = 'Unit test :: Orchestrator :: Test 11 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'SOUTH'}
        init = 0
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 0, 'f': 'SOUTH'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_12_robot_not_fall_east(self, keyboard):
        print('Functional test :: Orchestrator :: Test 12 :: Check '
              'the robot does not fall from East edge')
        error = 'Unit test :: Orchestrator :: Test 12 :: Failed'
        current_position = {'x': 4, 'y': 0, 'f': 'EAST'}
        init = 0
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 4, 'y': 0, 'f': 'EAST'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_13_robot_not_fall_north(self, keyboard):
        print('Functional test :: Orchestrator :: Test 13 :: Check '
              'the robot does not fall from West edge')
        error = 'Unit test :: Orchestrator :: Test 13 :: Failed'
        current_position = {'x': 0, 'y': 4, 'f': 'WEST'}
        init = 0
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 4, 'f': 'WEST'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_14_random_sequence(self, keyboard):
        print('Functional test :: Orchestrator :: Test 14 :: Check '
              'random sequence (1)')
        error = 'Unit test :: Orchestrator :: Test 14 :: Failed'
        current_position = {'x': None, 'y': None, 'f': None}
        init = 0
        keyboard.return_value = 'PLACE 0,0,NORTH'
        current_position, init = self.robot.run_game(current_position, init)
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        keyboard.return_value = 'RIGHT'
        current_position, init = self.robot.run_game(current_position, init)
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        keyboard.return_value = 'REPORT'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 1, 'y': 1, 'f': 'EAST'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_15_random_sequence(self, keyboard):
        print('Functional test :: Orchestrator :: Test 15 :: Check '
              'random sequence (2)')
        error = 'Unit test :: Orchestrator :: Test 15 :: Failed'
        current_position = {'x': 0, 'y': 2, 'f': 'WEST'}
        init = 0
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        keyboard.return_value = 'RIGHT'
        current_position, init = self.robot.run_game(current_position, init)
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        keyboard.return_value = 'RIGHT'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 4, 'f': 'EAST'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_16_random_sequence(self, keyboard):
        print('Functional test :: Orchestrator :: Test 16 :: Check '
              'random sequence (3)')
        error = 'Unit test :: Orchestrator :: Test 14 :: Failed'
        current_position = {'x': None, 'y': None, 'f': None}
        init = 0
        keyboard.return_value = 'PLACE 3,0,SOUTH'
        current_position, init = self.robot.run_game(current_position, init)
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        keyboard.return_value = 'RIGHT'
        current_position, init = self.robot.run_game(current_position, init)
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 1, 'y': 0, 'f': 'WEST'}
        self.assertEqual(current_position, out, error)
