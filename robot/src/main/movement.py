from robot.src.exceptions.fall_exception import FallException


class Movement(object):

    # This method is going to be used to move the robot around the surface
    # of the table
    @staticmethod
    def move(current_pos):
        try:

            # Move the Robot to the North if it is not going to fall
            if current_pos['f'] == 'NORTH' and current_pos['y'] < 4:
                current_pos['y'] += 1

            # Move the Robot to the West if it is not going to fall
            elif current_pos['f'] == 'EAST' and current_pos['x'] < 4:
                current_pos['x'] += 1

            # Move the Robot to the South if it is not going to fall
            elif current_pos['f'] == 'SOUTH' and current_pos['y'] > 0:
                current_pos['y'] -= 1

            # Move the Robot to the East if it is not going to fall
            elif current_pos['f'] == 'WEST' and current_pos['x'] > 0:
                current_pos['x'] -= 1

            else:
                raise FallException('Robot cannot fall')
            # Save robot's position
            res = current_pos

        # Manage exceptions
        except Exception as ex:
            raise ex

        # Return the current Robot's position
        return res
