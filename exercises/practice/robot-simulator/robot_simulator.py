# Globals for the directions
# Change the values as you see fit
EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self._direction = direction
        self._x_pos = x_pos
        self._y_pos = y_pos

    @property
    def coordinates(self):
        return self._x_pos, self._y_pos

    @property
    def direction(self):
        return self._direction

    def move(self, instructions):
        for instruction in instructions:
            if instruction == "R":
                self._turn_right()
            elif instruction == "L":
                self._turn_left()
            elif instruction == "A":
                self._advance()

    def _turn_right(self):
        if self._direction == NORTH:
            self._direction = EAST
        elif self._direction == EAST:
            self._direction = SOUTH
        elif self._direction == SOUTH:
            self._direction = WEST
        elif self._direction == WEST:
            self._direction = NORTH

    def _turn_left(self):
        if self._direction == NORTH:
            self._direction = WEST
        elif self._direction == WEST:
            self._direction = SOUTH
        elif self._direction == SOUTH:
            self._direction = EAST
        elif self._direction == EAST:
            self._direction = NORTH

    def _advance(self):
        if self._direction == NORTH:
            self._y_pos += 1
        elif self._direction == EAST:
            self._x_pos += 1
        elif self._direction == SOUTH:
            self._y_pos -= 1
        elif self._direction == WEST:
            self._x_pos -= 1
