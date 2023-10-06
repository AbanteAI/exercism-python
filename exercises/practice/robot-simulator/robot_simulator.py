# Globals for the directions
# Change the values as you see fit
EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)


class Robot:
        self.direction = direction
        self.x = x_pos
        self.y = y_pos
    def turn_right(self):
        directions = [NORTH, EAST, SOUTH, WEST]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]

    def turn_left(self):
        directions = [NORTH, EAST, SOUTH, WEST]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index - 1) % 4]

    def advance(self):
        self.x += self.direction[0]
        self.y += self.direction[1]