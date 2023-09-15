# Globals for the directions
# Change the values as you see fit
EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
    @property
    def coordinates(self):
        return (self.x_pos, self.y_pos)
    def turn_right(self):
        directions = [NORTH, EAST, SOUTH, WEST]
        index = (directions.index(self.direction) + 1) % 4
        self.direction = directions[index]

    def turn_left(self):
        directions = [NORTH, EAST, SOUTH, WEST]
        index = (directions.index(self.direction) - 1) % 4
        self.direction = directions[index]

    def advance(self):
        self.x_pos += self.direction[0]
        self.y_pos += self.direction[1]

    def move(self, instructions):
        for instruction in instructions:
            if instruction == "R":
                self.turn_right()
            elif instruction == "L":
                self.turn_left()
            elif instruction == "A":
                self.advance()
            else:
                raise ValueError("Invalid instruction")
