import unittest
from mock import patch

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


if __name__ == "__main__":
    unittest.main()
