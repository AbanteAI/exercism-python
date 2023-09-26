class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        pass



class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.read_index = 0
        self.write_index = 0
        self.is_full = False

    def read(self):
        if self.is_empty():
            raise BufferEmptyException("Buffer is empty")
        data = self.buffer[self.read_index]
        self.buffer[self.read_index] = None
        self.read_index = (self.read_index + 1) % self.capacity
        self.is_full = False
        return data

    def write(self, data):
        if self.is_full:
            raise BufferFullException("Buffer is full")
        self.buffer[self.write_index] = data
        self.write_index = (self.write_index + 1) % self.capacity
        if self.write_index == self.read_index:
            self.is_full = True

    def overwrite(self, data):
        if self.is_full:
            self.buffer[self.read_index] = data
            self.read_index = (self.read_index + 1) % self.capacity
            self.write_index = (self.write_index + 1) % self.capacity
        else:
            self.write(data)

    def clear(self):
        self.buffer = [None] * self.capacity
        self.read_index = 0
        self.write_index = 0
        self.is_full = False