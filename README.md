# # # # # # #
# TOY_ROBOT #
# # # # # # #
 

GAME DESCRIPTION:

- The application is a simulation of a toy robot moving on a square tabletop,
  of dimensions 5 units x 5 units.
- There are no other obstructions on the table surface.
- The robot is free to roam around the surface of the table, but cannot fall.
  Any movement that would result in the robot falling from the table is
  prevented, however further valid movement commands are still allowed.



INSTRUCTIONS:

Commands:

  - PLACE X,Y,F
  - MOVE
  - LEFT
  - RIGHT
  - REPORT


Explanation:

  - PLACE will put the toy robot on the table in position X,Y and facing
    NORTH, SOUTH, EAST or WEST.
  - MOVE will move the toy robot one unit forward in the direction it is
    currently facing.
  - LEFT and RIGHT will rotate the robot 90 degrees in the specified
    direction without changing the position of the robot.
  - REPORT will announce the X,Y and F of the robot.
  - The origin (0,0) is the SOUTH WEST most corner.
  - The first valid command to the robot is a PLACE command, after that, any
    sequence of commands may be issued, in any order, including another
    PLACE command. The application discard all commands in the sequence
    until a valid PLACE command has been executed.



ARCHITECTURE:

Modules:

  - Rotation: Rotates 90º the robot to the right or to the left. Return the
    new Cardinal Point the robot is facing. Returns the new Cardinal Point.
  - Placement: Places the robot and returns the new position of the robot.
  - Movement: Moves the robot and check it cannot fall. Returns the new
    position.
  - Inputs: Treats the input. It makes sure that the actions and the Cardinal
    Points exists, and the new position is between the limits. Besides it
    checks that the commands do not have arguments, but PLACE. Returns the
    command and the arguments.
  - Orchestrator: Main module. Organize the rest of the modules and runs the
    game. Also it checks that the game is already started. Returns the new
    position and the state of the game (started or not started).


Tests:

  - Unit test.
  - Integration test.
  - Functional test.


Exceptions:

  - LimitException: Position introduced is out of the limits of the table.
  - StartException: The robot has not been placed yet, therefore actions
    cannot be done, except Place.
  - FallException: The robot cannot move because if it moves it falls.
  - ActionException: The action does not exists.
  - FacedException: The Cardinal Point does not exist.
  - ArgsException: Commands MOVE, RIGHT, LEFT and REPORT do not have
    arguments.
