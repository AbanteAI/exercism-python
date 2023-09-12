class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
        self.message = message
        super().__init__(self.message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
        self.message = message
        super().__init__(self.message)


class CircularBuffer:
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.read_pos = 0
        self.write_pos = 0

        if self.buffer[self.read_pos] is None:
            raise BufferEmptyException("Circular buffer is empty")
        data = self.buffer[self.read_pos]
        self.buffer[self.read_pos] = None
        self.read_pos = (self.read_pos + 1) % self.capacity
        return data

        if self.buffer[self.write_pos] is not None:
            raise BufferFullException("Circular buffer is full")
        self.buffer[self.write_pos] = data
        self.write_pos = (self.write_pos + 1) % self.capacity

        self.buffer[self.write_pos] = data
        self.write_pos = (self.write_pos + 1) % self.capacity
        if self.buffer[self.read_pos] is not None:
            self.read_pos = (self.read_pos + 1) % self.capacity

        self.buffer = [None] * self.capacity
        self.read_pos = 0
        self.write_pos = 0
