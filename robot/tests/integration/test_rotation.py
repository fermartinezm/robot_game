import unittest

from robot.src.main.rotation import Rotation


class TestRotation(unittest.TestCase):

    def setUp(self):
        self.__CURRENT_POS = {'x': 2, 'y': 2, 'f': 'NORTH'}
        self.__ROTATE = {'direc': 'RIGHT'}
        self.robot = Rotation()

    def tearDown(self):
        """Override tearDown."""
        pass

    def test_01_rotate_right_to_east(self):
        print('Unit test :: Rotation :: Test 01 :: '
              'Rotate robot from NORTH to EAST')
        error = 'Unit test :: Rotation :: Test 01 :: Failed'
        result = self.robot.rotate(self.__ROTATE, self.__CURRENT_POS)
        self.assertEqual(result['f'], 'EAST', error)

    def test_02_rotate_right_to_south(self):
        print('Unit test :: Rotation :: Test 02 :: '
              'Rotate robot from EAST to SOUTH')
        error = 'Unit test :: Rotation :: Test 02 :: Failed'
        self.__CURRENT_POS['f'] = 'EAST'
        result = self.robot.rotate(self.__ROTATE, self.__CURRENT_POS)
        self.assertEqual(result['f'], 'SOUTH', error)

    def test_03_rotate_right_to_west(self):
        print('Unit test :: Rotation :: Test 03 :: '
              'Rotate robot from SOUTH to WEST')
        error = 'Unit test :: Rotation :: Test 03 :: Failed'
        self.__CURRENT_POS['f'] = 'SOUTH'
        result = self.robot.rotate(self.__ROTATE, self.__CURRENT_POS)
        self.assertEqual(result['f'], 'WEST', error)

    def test_04_rotate_right_to_nort(self):
        print('Unit test :: Rotation :: Test 04 :: '
              'Rotate robot from WEST to NORTH')
        error = 'Unit test :: Rotation :: Test 04 :: Failed'
        self.__CURRENT_POS['f'] = 'WEST'
        result = self.robot.rotate(self.__ROTATE, self.__CURRENT_POS)
        self.assertEqual(result['f'], 'NORTH', error)

    def test_05_rotate_left_to_west(self):
        print('Unit test :: Rotation :: Test 05 :: '
              'Rotate robot from NORTH to WEST')
        error = 'Unit test :: Rotation :: Test 05 :: Failed'
        self.__ROTATE['direc'] = 'LEFT'
        result = self.robot.rotate(self.__ROTATE, self.__CURRENT_POS)
        self.assertEqual(result['f'], 'WEST', error)

    def test_06_rotate_left_to_south(self):
        print('Unit test :: Rotation :: Test 06 :: '
              'Rotate robot from WEST to SOUTH')
        error = 'Unit test :: Rotation :: Test 06 :: Failed'
        self.__CURRENT_POS['f'] = 'WEST'
        self.__ROTATE['direc'] = 'LEFT'
        result = self.robot.rotate(self.__ROTATE, self.__CURRENT_POS)
        self.assertEqual(result['f'], 'SOUTH', error)

    def test_07_rotate_left_to_east(self):
        print('Unit test :: Rotation :: Test 07 :: '
              'Rotate robot from SOUTH to EAST')
        error = 'Unit test :: Rotation :: Test 07 :: Failed'
        self.__CURRENT_POS['f'] = 'SOUTH'
        self.__ROTATE['direc'] = 'LEFT'
        result = self.robot.rotate(self.__ROTATE, self.__CURRENT_POS)
        self.assertEqual(result['f'], 'EAST', error)

    def test_08_rotate_left_to_north(self):
        print('Unit test :: Rotation :: Test 08 :: '
              'Rotate robot from EAST to NORTH')
        error = 'Unit test :: Rotation :: Test 08 :: Failed'
        self.__CURRENT_POS['f'] = 'EAST'
        self.__ROTATE['direc'] = 'LEFT'
        result = self.robot.rotate(self.__ROTATE, self.__CURRENT_POS)
        self.assertEqual(result['f'], 'NORTH', error)


if __name__ == "__main__":
    unittest.main()
