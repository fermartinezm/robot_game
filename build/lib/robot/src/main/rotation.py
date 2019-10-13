class Rotation(object):

    def __init__(self):
        self.aux = {
            0: 'NORTH',
            1: 'EAST',
            2: 'SOUTH',
            3: 'WEST'
        }

    # This method is going to associate the current direction with
    # a key from the dic "aux"
    def current_orientation(self, current_pos):
        for aux_key, aux_face in self.aux.items():
            if aux_face == current_pos['f']:
                return aux_key

    # This method is going to rotate the robot
    def rotate(self, direction, current_pos):
        try:

            # Rotate robot to the left
            if direction['direc'] == 'LEFT':
                current_pos['f'] = self.aux[(
                    self.current_orientation(current_pos) - 1) % 4]

            # Rotate robot to the right
            elif direction['direc'] == 'RIGHT':
                current_pos['f'] = self.aux[(
                    self.current_orientation(current_pos) + 1) % 4]

            res = current_pos

        except Exception as ex:
            raise ex

        return res
