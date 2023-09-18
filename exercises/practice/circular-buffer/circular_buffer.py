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
    def __init__(self, message):
        super().__init__(message)


class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = [None] * capacity
        self.capacity = capacity
        self.start = 0
        self.end = 0

    def read(self):
        if self.buffer[self.start] is None:
            raise BufferEmptyException("Circular buffer is empty")
        value = self.buffer[self.start]
        self.buffer[self.start] = None
        self.start = (self.start + 1) % self.capacity
        return value

    def write(self, data):
        if self.buffer[self.end] is not None:
            raise BufferFullException("Circular buffer is full")
        self.buffer[self.end] = data
        self.end = (self.end + 1) % self.capacity

        if self.buffer[self.end] is None:
            self.write(data)
        else:
            self.buffer[self.start] = data
            self.start = (self.start + 1) % self.capacity
            self.end = (self.end + 1) % self.capacity

    def clear(self):
        self.buffer = [None] * self.capacity
        self.start = 0
        self.end = 0
