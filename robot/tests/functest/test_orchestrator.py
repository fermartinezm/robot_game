import unittest
from mock import patch

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
    def test_06_move_robot_north(self, keyboard):
        print('Functional test :: Orchestrator :: Test 06 :: Check '
              'MOVE action to the North when the robot has been placed')
        error = 'Unit test :: Orchestrator :: Test 06 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'NORTH'}
        init = 0
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 1, 'f': 'NORTH'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_07_move_robot_east(self, keyboard):
        print('Functional test :: Orchestrator :: Test 07 :: Check '
              'MOVE action to the East when the robot has been placed')
        error = 'Unit test :: Orchestrator :: Test 07 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'EAST'}
        init = 0
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 1, 'y': 0, 'f': 'EAST'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_08_move_robot_south(self, keyboard):
        print('Functional test :: Orchestrator :: Test 08 :: Check '
              'MOVE action to the South when the robot has been placed')
        error = 'Unit test :: Orchestrator :: Test 08 :: Failed'
        current_position = {'x': 0, 'y': 4, 'f': 'SOUTH'}
        init = 0
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 3, 'f': 'SOUTH'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_09_move_robot_west(self, keyboard):
        print('Functional test :: Orchestrator :: Test 09 :: Check '
              'MOVE action to the West when the robot has been placed')
        error = 'Unit test :: Orchestrator :: Test 09 :: Failed'
        current_position = {'x': 4, 'y': 4, 'f': 'WEST'}
        init = 0
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 3, 'y': 4, 'f': 'WEST'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_10_right_robot_east(self, keyboard):
        print('Functional test :: Orchestrator :: Test 10 :: Check '
              'RIGHT action to the East when the robot has been placed')
        error = 'Unit test :: Orchestrator :: Test 10 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'NORTH'}
        init = 0
        keyboard.return_value = 'RIGHT'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 0, 'f': 'EAST'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_11_right_robot_south(self, keyboard):
        print('Functional test :: Orchestrator :: Test 11 :: Check '
              'RIGHT action to the South when the robot has been placed')
        error = 'Unit test :: Orchestrator :: Test 11 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'EAST'}
        init = 0
        keyboard.return_value = 'RIGHT'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 0, 'f': 'SOUTH'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_12_right_robot_west(self, keyboard):
        print('Functional test :: Orchestrator :: Test 12 :: Check '
              'RIGHT action to the West when the robot has been placed')
        error = 'Unit test :: Orchestrator :: Test 12 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'SOUTH'}
        init = 0
        keyboard.return_value = 'RIGHT'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 0, 'f': 'WEST'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_13_right_robot_north(self, keyboard):
        print('Functional test :: Orchestrator :: Test 13 :: Check '
              'RIGHT action to the North when the robot has been placed')
        error = 'Unit test :: Orchestrator :: Test 13 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'WEST'}
        init = 0
        keyboard.return_value = 'RIGHT'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 0, 'f': 'NORTH'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_14_left_robot_west(self, keyboard):
        print('Functional test :: Orchestrator :: Test 14 :: Check '
              'LEFT action to the West when the robot has been placed')
        error = 'Unit test :: Orchestrator :: Test 14 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'NORTH'}
        init = 0
        keyboard.return_value = 'LEFT'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 0, 'f': 'WEST'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_15_left_robot_south(self, keyboard):
        print('Functional test :: Orchestrator :: Test 15 :: Check '
              'LEFT action to the South when the robot has been placed')
        error = 'Unit test :: Orchestrator :: Test 15 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'WEST'}
        init = 0
        keyboard.return_value = 'LEFT'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 0, 'f': 'SOUTH'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_16_left_robot_east(self, keyboard):
        print('Functional test :: Orchestrator :: Test 16 :: Check '
              'LEFT action to the East when the robot has been placed')
        error = 'Unit test :: Orchestrator :: Test 16 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'SOUTH'}
        init = 0
        keyboard.return_value = 'LEFT'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 0, 'f': 'EAST'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_17_left_robot_north(self, keyboard):
        print('Functional test :: Orchestrator :: Test 17 :: Check '
              'LEFT action to the North when the robot has been placed')
        error = 'Unit test :: Orchestrator :: Test 17 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'EAST'}
        init = 0
        keyboard.return_value = 'LEFT'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 0, 'f': 'NORTH'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_18_report_robot(self, keyboard):
        print('Functional test :: Orchestrator :: Test 18 :: Check '
              'REPORT action when the robot has been placed')
        error = 'Unit test :: Orchestrator :: Test 18 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'NORTH'}
        init = 0
        keyboard.return_value = 'REPORT'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 0, 'f': 'NORTH'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_19_robot_not_fall_north(self, keyboard):
        print('Functional test :: Orchestrator :: Test 19 :: Check '
              'the robot does not fall from North edge')
        error = 'Unit test :: Orchestrator :: Test 19 :: Failed'
        current_position = {'x': 0, 'y': 4, 'f': 'NORTH'}
        init = 0
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 4, 'f': 'NORTH'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_20_robot_not_fall_south(self, keyboard):
        print('Functional test :: Orchestrator :: Test 20 :: Check '
              'the robot does not fall from South edge')
        error = 'Unit test :: Orchestrator :: Test 20 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'SOUTH'}
        init = 0
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 0, 'f': 'SOUTH'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_21_robot_not_fall_east(self, keyboard):
        print('Functional test :: Orchestrator :: Test 21 :: Check '
              'the robot does not fall from East edge')
        error = 'Unit test :: Orchestrator :: Test 21 :: Failed'
        current_position = {'x': 4, 'y': 0, 'f': 'EAST'}
        init = 0
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 4, 'y': 0, 'f': 'EAST'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_22_robot_not_fall_west(self, keyboard):
        print('Functional test :: Orchestrator :: Test 22 :: Check '
              'the robot does not fall from West edge')
        error = 'Unit test :: Orchestrator :: Test 22 :: Failed'
        current_position = {'x': 0, 'y': 4, 'f': 'WEST'}
        init = 0
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 4, 'f': 'WEST'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_23_random_sequence(self, keyboard):
        print('Functional test :: Orchestrator :: Test 23 :: Check '
              'random sequence (1)')
        error = 'Unit test :: Orchestrator :: Test 23 :: Failed'
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
    def test_24_random_sequence(self, keyboard):
        print('Functional test :: Orchestrator :: Test 24 :: Check '
              'random sequence (2)')
        error = 'Unit test :: Orchestrator :: Test 24 :: Failed'
        current_position = {'x': 0, 'y': 2, 'f': 'WEST'}
        init = 0
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        keyboard.return_value = 'LEFT'
        current_position, init = self.robot.run_game(current_position, init)
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        keyboard.return_value = 'LEFT'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 0, 'f': 'EAST'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_25_random_sequence(self, keyboard):
        print('Functional test :: Orchestrator :: Test 25 :: Check '
              'random sequence (3)')
        error = 'Unit test :: Orchestrator :: Test 25 :: Failed'
        current_position = {'x': None, 'y': None, 'f': None}
        init = 0
        keyboard.return_value = 'PLACE 3,0,SOUTH'
        current_position, init = self.robot.run_game(current_position, init)
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        keyboard.return_value = 'PLACE 2,2,EAST'
        current_position, init = self.robot.run_game(current_position, init)
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        keyboard.return_value = 'MOVE'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 4, 'y': 2, 'f': 'EAST'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_26_check_position_below_limit(self, keyboard):
        print('Functional test :: Orchestrator :: Test 26 :: Check '
              'position below the limit')
        error = 'Unit test :: Orchestrator :: Test 26 :: Failed'
        current_position = {'x': None, 'y': None, 'f': None}
        init = 0
        keyboard.return_value = 'PLACE -3,0,SOUTH'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': None, 'y': None, 'f': None}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_27_check_position_above_limit(self, keyboard):
        print('Functional test :: Orchestrator :: Test 26 :: Check '
              'position above the limit')
        error = 'Unit test :: Orchestrator :: Test 26 :: Failed'
        current_position = {'x': None, 'y': None, 'f': None}
        init = 0
        keyboard.return_value = 'PLACE 0,7,SOUTH'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': None, 'y': None, 'f': None}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_28_place_action_no_args(self, keyboard):
        print('Functional test :: Orchestrator :: Test 28 :: Check '
              'PLACE action with no arguments')
        error = 'Unit test :: Orchestrator :: Test 28 :: Failed'
        current_position = {'x': None, 'y': None, 'f': None}
        init = 0
        keyboard.return_value = 'PLACE'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': None, 'y': None, 'f': None}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_29_place_wrong_args_data_type(self, keyboard):
        print('Functional test :: Orchestrator :: Test 29 :: Check '
              'PLACE action with wrong arguments')
        error = 'Unit test :: Orchestrator :: Test 29 :: Failed'
        current_position = {'x': None, 'y': None, 'f': None}
        init = 0
        keyboard.return_value = 'PLACE asd,asd,asda'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': None, 'y': None, 'f': None}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_30_check_move_with_args(self, keyboard):
        print('Functional test :: Orchestrator :: Test 30 :: Check '
              'MOVE action with arguments')
        error = 'Unit test :: Orchestrator :: Test 30 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'NORTH'}
        init = 0
        keyboard.return_value = 'MOVE asd,asd,asda'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 0, 'f': 'NORTH'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_31_check_left_with_args(self, keyboard):
        print('Functional test :: Orchestrator :: Test 31 :: Check '
              'LEFT action with arguments')
        error = 'Unit test :: Orchestrator :: Test 31 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'NORTH'}
        init = 0
        keyboard.return_value = 'LEFT asd,asd,asda'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 0, 'f': 'NORTH'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_32_check_move_with_args(self, keyboard):
        print('Functional test :: Orchestrator :: Test 32 :: Check '
              'RIGHT action with arguments')
        error = 'Unit test :: Orchestrator :: Test 32 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'NORTH'}
        init = 0
        keyboard.return_value = 'RIGHT asd,asd,asda'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 0, 'f': 'NORTH'}
        self.assertEqual(current_position, out, error)

    @patch('robot.src.main.orchestrator.Orchestrator.get_input')
    def test_33_check_report_with_args(self, keyboard):
        print('Functional test :: Orchestrator :: Test 33 :: Check '
              'REPORT action with arguments')
        error = 'Unit test :: Orchestrator :: Test 33 :: Failed'
        current_position = {'x': 0, 'y': 0, 'f': 'NORTH'}
        init = 0
        keyboard.return_value = 'MOVE asd,asd,asda'
        current_position, init = self.robot.run_game(current_position, init)
        out = {'x': 0, 'y': 0, 'f': 'NORTH'}
        self.assertEqual(current_position, out, error)


if __name__ == "__main__":
    unittest.main()
