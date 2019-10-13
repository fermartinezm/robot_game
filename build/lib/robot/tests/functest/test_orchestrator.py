import unittest

from robot.src.exceptions.start_exception import StartException
from robot.src.main.orchestrator import Orchestrator


class TestInOut(unittest.TestCase):

    def setUp(self):
        self.__INPUT = 'PLACE 0,0,NORTH'
        self.robot = Orchestrator()

    def tearDown(self):
        """Override tearDown."""
        pass

    def test_01_move_action_not_placed_robot(self):
        print('Functional test :: Orchestrator :: Test 06 :: Do not realize '
              'the action when the robot is not still placed')
        print(self.robot(self.__INPUT))
