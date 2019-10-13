import unittest
from mock import patch

from robot.src.main.rotation import Rotation


class TestRotation(unittest.TestCase):

    def setUp(self):
        self.__CURRENT_POS = {'x': 2, 'y': 2, 'f': 'NORTH'}
        self.__ROTATE = {'direc': 'RIGHT'}
        self.robot = Rotation()

    def tearDown(self):
        """Override tearDown."""
        pass

    @patch('robot.src.main.rotation.Rotation.current_orientation')
    def test_01_rotate_right_to_east(self, orientation):
        print('Integration test :: Rotation :: Test 01 :: '
              'Rotate robot from NORTH to EAST')
        error = 'Unit test :: Rotation :: Test 01 :: Failed'
        orientation.return_value = 0
        result = self.robot.rotate(self.__ROTATE, self.__CURRENT_POS)
        self.assertEqual(result['f'], 'EAST', error)

    @patch('robot.src.main.rotation.Rotation.current_orientation')
    def test_02_rotate_right_to_south(self, orientation):
        print('Integration test :: Rotation :: Test 02 :: '
              'Rotate robot from EAST to SOUTH')
        error = 'Unit test :: Rotation :: Test 02 :: Failed'
        self.__CURRENT_POS['f'] = 'EAST'
        orientation.return_value = 1
        result = self.robot.rotate(self.__ROTATE, self.__CURRENT_POS)
        self.assertEqual(result['f'], 'SOUTH', error)

    @patch('robot.src.main.rotation.Rotation.current_orientation')
    def test_03_rotate_right_to_west(self, orientation):
        print('Integration test :: Rotation :: Test 03 :: '
              'Rotate robot from SOUTH to WEST')
        error = 'Unit test :: Rotation :: Test 03 :: Failed'
        self.__CURRENT_POS['f'] = 'SOUTH'
        orientation.return_value = 2
        result = self.robot.rotate(self.__ROTATE, self.__CURRENT_POS)
        self.assertEqual(result['f'], 'WEST', error)

    @patch('robot.src.main.rotation.Rotation.current_orientation')
    def test_04_rotate_right_to_north(self, orientation):
        print('Integration test :: Rotation :: Test 04 :: '
              'Rotate robot from WEST to NORTH')
        error = 'Unit test :: Rotation :: Test 04 :: Failed'
        self.__CURRENT_POS['f'] = 'WEST'
        orientation.return_value = 3
        result = self.robot.rotate(self.__ROTATE, self.__CURRENT_POS)
        self.assertEqual(result['f'], 'NORTH', error)

    @patch('robot.src.main.rotation.Rotation.current_orientation')
    def test_05_rotate_left_to_west(self, orientation):
        print('Integration test :: Rotation :: Test 05 :: '
              'Rotate robot from NORTH to WEST')
        error = 'Unit test :: Rotation :: Test 05 :: Failed'
        self.__ROTATE['direc'] = 'LEFT'
        orientation.return_value = 0
        result = self.robot.rotate(self.__ROTATE, self.__CURRENT_POS)
        self.assertEqual(result['f'], 'WEST', error)

    @patch('robot.src.main.rotation.Rotation.current_orientation')
    def test_06_rotate_left_to_south(self, orientation):
        print('Integration test :: Rotation :: Test 06 :: '
              'Rotate robot from WEST to SOUTH')
        error = 'Unit test :: Rotation :: Test 06 :: Failed'
        self.__CURRENT_POS['f'] = 'WEST'
        self.__ROTATE['direc'] = 'LEFT'
        orientation.return_value = 3
        result = self.robot.rotate(self.__ROTATE, self.__CURRENT_POS)
        self.assertEqual(result['f'], 'SOUTH', error)

    @patch('robot.src.main.rotation.Rotation.current_orientation')
    def test_07_rotate_left_to_east(self, orientation):
        print('Integration test :: Rotation :: Test 07 :: '
              'Rotate robot from SOUTH to EAST')
        error = 'Unit test :: Rotation :: Test 07 :: Failed'
        self.__CURRENT_POS['f'] = 'SOUTH'
        self.__ROTATE['direc'] = 'LEFT'
        orientation.return_value = 2
        result = self.robot.rotate(self.__ROTATE, self.__CURRENT_POS)
        self.assertEqual(result['f'], 'EAST', error)

    @patch('robot.src.main.rotation.Rotation.current_orientation')
    def test_08_rotate_left_to_north(self, orientation):
        print('Integration test :: Rotation :: Test 08 :: '
              'Rotate robot from EAST to NORTH')
        error = 'Unit test :: Rotation :: Test 08 :: Failed'
        self.__CURRENT_POS['f'] = 'EAST'
        self.__ROTATE['direc'] = 'LEFT'
        orientation.return_value = 1
        result = self.robot.rotate(self.__ROTATE, self.__CURRENT_POS)
        self.assertEqual(result['f'], 'NORTH', error)

    def test_09_check_orientation_key_0(self):
        print('Integration test :: Rotation :: Test 09 :: '
              'Check current_orientation method. 0: "NORTH"')
        error = 'Unit test :: Rotation :: Test 09 :: Failed'
        result = self.robot.current_orientation(self.__CURRENT_POS)
        self.assertEqual(result, 0, error)

    def test_10_check_orientation_key_1(self):
        print('Integration test :: Rotation :: Test 10 :: '
              'Check current_orientation method. 1: "EAST"')
        error = 'Unit test :: Rotation :: Test 10 :: Failed'
        self.__CURRENT_POS['f'] = 'EAST'
        result = self.robot.current_orientation(self.__CURRENT_POS)
        self.assertEqual(result, 1, error)

    def test_11_check_orientation_key_2(self):
        print('Integration test :: Rotation :: Test 11 :: '
              'Check current_orientation method. 2: "SOUTH"')
        error = 'Unit test :: Rotation :: Test 11 :: Failed'
        self.__CURRENT_POS['f'] = 'SOUTH'
        result = self.robot.current_orientation(self.__CURRENT_POS)
        self.assertEqual(result, 2, error)

    def test_12_check_orientation_key_3(self):
        print('Integration test :: Rotation :: Test 12 :: '
              'Check current_orientation method. 3: "WEST"')
        error = 'Unit test :: Rotation :: Test 12 :: Failed'
        self.__CURRENT_POS['f'] = 'WEST'
        result = self.robot.current_orientation(self.__CURRENT_POS)
        self.assertEqual(result, 3, error)


if __name__ == "__main__":
    unittest.main()
