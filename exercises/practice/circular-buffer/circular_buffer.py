class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        super().__init__(message)

class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
        super().__init__(message)
    def __init__(self, message):
        super().__init__(message)
class CircularBuffer:
        self.buffer = [None] * capacity
        self.capacity = capacity
    def __init__(self, capacity):
        self.buffer = [None] * capacity
        self.capacity = capacity
        self.start = 0
        self.end = 0
        self.size = 0

    def read(self):
        if self.size == 0:
            raise BufferEmptyException("Circular buffer is empty")
        value = self.buffer[self.start]
        self.buffer[self.start] = None
        self.start = (self.start + 1) % self.capacity
        self.size -= 1
        return value

    def write(self, data):
        if self.size == self.capacity:
            raise BufferFullException("Circular buffer is full")
        self.buffer[self.end] = data
        self.end = (self.end + 1) % self.capacity
        self.size += 1

    def overwrite(self, data):
        if self.size == self.capacity:
            self.start = (self.start + 1) % self.capacity
        else:
            self.size += 1
        self.buffer[self.end] = data
        self.end = (self.end + 1) % self.capacity

    def clear(self):
        self.buffer = [None] * self.capacity
        self.start = 0
        self.end = 0
        self.size = 0