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
        self.head = 0
        self.tail = 0

    def read(self):
        if self.buffer[self.head] is None:
            raise BufferEmptyException("Circular buffer is empty")
        value = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        return value

    def write(self, data):
        if self.buffer[self.tail] is not None:
            raise BufferFullException("Circular buffer is full")
        self.buffer[self.tail] = data
        self.tail = (self.tail + 1) % self.capacity

    def overwrite(self, data):
        if self.buffer[self.tail] is None:
            self.write(data)
        else:
            self.buffer[self.tail] = data
            self.tail = (self.tail + 1) % self.capacity
            self.head = (self.head + 1) % self.capacity

    def clear(self):
        self.buffer = [None] * self.capacity
        self.head = 0
        self.tail = 0
