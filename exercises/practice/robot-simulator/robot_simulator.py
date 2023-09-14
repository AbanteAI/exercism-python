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
        return self.x_pos, self.y_pos

    def move(self, instructions):
        for instruction in instructions:
            if instruction == "L":
                self.direction = (self.direction[1], -self.direction[0])
            elif instruction == "R":
                self.direction = (-self.direction[1], self.direction[0])
            elif instruction == "A":
                self.x_pos += self.direction[0]
                self.y_pos += self.direction[1]
            else:
                raise ValueError("Invalid instruction")
