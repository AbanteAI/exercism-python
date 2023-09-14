class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
        super().__init__(message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
        super().__init__(message)


class CircularBuffer:
        self.buffer = [None] * capacity
        self.capacity = capacity
        self.read_pos = 0
        self.write_pos = 0
        self.is_full = False

        if self.buffer[self.read_pos] is None:
            raise BufferEmptyException("Circular buffer is empty")
        value = self.buffer[self.read_pos]
        self.buffer[self.read_pos] = None
        self.read_pos = (self.read_pos + 1) % self.capacity
        self.is_full = False
        return value

        if self.is_full:
            raise BufferFullException("Circular buffer is full")
        self.buffer[self.write_pos] = data
        self.write_pos = (self.write_pos + 1) % self.capacity
        if self.write_pos == self.read_pos:
            self.is_full = True

        self.buffer[self.write_pos] = data
        self.write_pos = (self.write_pos + 1) % self.capacity
        if self.buffer[self.read_pos] is not None:
            self.read_pos = (self.read_pos + 1) % self.capacity

        self.buffer = [None] * self.capacity
        self.read_pos = 0
        self.write_pos = 0
        self.is_full = False
