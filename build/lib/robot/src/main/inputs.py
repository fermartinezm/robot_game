from robot.src.exceptions.action_exception import ActionException
from robot.src.exceptions.limit_exception import LimitException
from robot.src.exceptions.faced_exception import FacedException
from robot.src.exceptions.args_exception import ArgsException


class Inputs(object):

    # Method to discard all the possibles inputs that are not correct.
    # If the input is correct, it is sent back to the orchestrator as a dict
    def treat_inputs(self, inputs):
        try:
            # Get action from the input and check that it exists
            action = inputs['inp'].split(' ')[0]
            checked_action = self.check_action(action)
            # If the action is place, get the arguments
            if action == 'PLACE':
                x, y, f = self.get_place_arguments(inputs)
                command = {'cmd': checked_action, 'x': x, 'y': y, 'f': f}
            else:
                try:
                    # Check if the action is not place and it has arguments
                    inputs['inp'].split(' ')[1]
                    # If the action is not place and has arguments
                    # discard the input (raising an exception)
                    raise ArgsException(
                        'This command should not have arguments')
                except ArgsException as ex:
                    raise ex
                # If the action is not place and it has not arguments
                # send back to the orchestrator as a dict
                except Exception:
                    command = {'cmd': checked_action}

        except Exception as ex:
            raise ex

        return command

    # Method to get and check the arguments from the input, if they are
    # not valid an exception is raised
    def get_place_arguments(self, inputs):
        try:
            x = int(inputs['inp'].split(' ')[1].split(',')[0])
            checked_x = self.check_limits(x)
            y = int(inputs['inp'].split(' ')[1].split(',')[1])
            checked_y = self.check_limits(y)
            faced = inputs['inp'].split(' ')[1].split(',')[2]
            checked_faced = self.check_faced(faced)

        except ValueError:
            raise Exception('Please, check arguments format and data type')
        except IndexError:
            raise Exception('Please, check arguments format and data type')
        except Exception as ex:
            raise ex

        return checked_x, checked_y, checked_faced

    # Method to check place position, if it is not valid an
    # exception is raised
    @staticmethod
    def check_limits(limit):
        try:
            if 0 > limit or limit > 4:
                raise LimitException(
                    'Please, coordinates should be between 0 and 4')

        except Exception as ex:
            raise ex

        return limit

    # Method to check the action, if it is not valid an
    # exception is raised
    @staticmethod
    def check_action(action):
        try:
            if action not in ['PLACE', 'MOVE', 'LEFT', 'RIGHT', 'REPORT']:
                raise ActionException('Please, insert an existing action')

        except Exception as ex:
            raise ex

        return action

    # Method to check cardinal point, if it is not valid an
    # exception is raised
    @staticmethod
    def check_faced(faced):
        try:
            if faced not in ['NORTH', 'EAST', 'SOUTH', 'WEST']:
                raise FacedException('Please, insert existing cardinal point')

        except Exception as ex:
            raise ex

        return faced

    '''# Method to print the current position of the robot
    @staticmethod
    def report(current_position):
        print(current_position)
        return current_position'''
