# Globals for the directions
# Change the values as you see fit
EAST = 'EAST'
NORTH = 'NORTH'
WEST = 'WEST'
SOUTH = 'SOUTH'


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.x = x
        self.y = y
    @property
    def coordinates(self):
        return (self.x, self.y)
    def turn_right(self):
        directions = [NORTH, EAST, SOUTH, WEST]
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def turn_left(self):
        directions = [NORTH, EAST, SOUTH, WEST]
        self.direction = directions[(directions.index(self.direction) - 1) % 4]

    def advance(self):
        if self.direction == NORTH:
            self.y += 1
        elif self.direction == EAST:
            self.x += 1
        elif self.direction == SOUTH:
            self.y -= 1
        elif self.direction == WEST:
            self.x -= 1

    def move(self, instructions):
        for instruction in instructions:
            if instruction == 'R':
                self.turn_right()
            elif instruction == 'L':
                self.turn_left()
            elif instruction == 'A':
                self.advance()
