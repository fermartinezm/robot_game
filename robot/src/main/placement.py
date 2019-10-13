class Placement(object):

    # Method to place the robot
    @staticmethod
    def place(command):
        try:
            # Place the robot if the desired position exists
            del command['cmd']

        except Exception as ex:
            raise ex

        return command
