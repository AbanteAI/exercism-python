# Globals for the directions
# Change the values as you see fit
EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)

class Robot:
        self.coordinates = (x_pos, y_pos)

    def move(self, instructions):
        for instruction in instructions:
            if instruction == "A":
                self.x_pos += self.direction[0]
                self.y_pos += self.direction[1]
            elif instruction == "L":
                self.direction = {
                    NORTH: WEST,
                    WEST: SOUTH,
                    SOUTH: EAST,
                    EAST: NORTH,
                }[self.direction]
            elif instruction == "R":
                self.direction = {
                    NORTH: EAST,
                    EAST: SOUTH,
                    SOUTH: WEST,
                    WEST: NORTH,
                }[self.direction]


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        pass
