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
        self.capacity = capacity
        self.buffer = []
        self.head = 0
        self.tail = 0
        self.count = 0

    def read(self):
        if self.count == 0:
            raise BufferEmptyException("Circular buffer is empty")
        value = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return value

    def write(self, data):
        if self.count == self.capacity:
            raise BufferFullException("Circular buffer is full")
        if self.count < self.capacity:
            if len(self.buffer) < self.capacity:
                self.buffer.append(data)
            else:
                self.buffer[self.tail] = data
            self.tail = (self.tail + 1) % self.capacity
            self.count += 1

    def overwrite(self, data):
        if self.count == self.capacity:
            self.buffer[self.head] = data
            self.head = (self.head + 1) % self.capacity
        else:
            self.write(data)

    def clear(self):
        self.buffer = []
        self.head = 0
        self.tail = 0
        self.count = 0
