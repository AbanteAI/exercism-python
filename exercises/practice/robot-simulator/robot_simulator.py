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
    def move(self):
        self.x_pos += self.direction[0]
        self.y_pos += self.direction[1]

    def turn_left(self):
        self.direction = (-self.direction[1], self.direction[0])

    def turn_right(self):
        self.direction = (self.direction[1], -self.direction[0])

    def simulate(self, instructions):
        for instruction in instructions:
            if instruction == "A":
                self.move()
            elif instruction == "L":
                self.turn_left()
            elif instruction == "R":
                self.turn_right()
            else:
                raise ValueError("Invalid instruction")
