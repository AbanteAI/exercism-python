# Globals for the directions
# Change the values as you see fit
EAST = None
NORTH = None
WEST = None
SOUTH = None


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
    def turn_right(self):
        if self.direction == NORTH:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = NORTH

    def turn_left(self):
        if self.direction == NORTH:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = NORTH

    def advance(self):
        if self.direction == NORTH:
            self.y_pos += 1
        elif self.direction == EAST:
            self.x_pos += 1
        elif self.direction == SOUTH:
            self.y_pos -= 1
        elif self.direction == WEST:
            self.x_pos -= 1