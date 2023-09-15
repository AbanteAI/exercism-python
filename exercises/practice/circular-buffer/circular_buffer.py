class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        pass


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        pass


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
    
    def read(self):
        if len(self.buffer) == 0:
            raise BufferEmptyException("Buffer is empty")
        return self.buffer.pop(0)
    
    def write(self, data):
        if len(self.buffer) == self.capacity:
            raise BufferFullException("Buffer is full")
        self.buffer.append(data)
    
    def overwrite(self, data):
        if len(self.buffer) == self.capacity:
            self.buffer.pop(0)
        self.buffer.append(data)
    
    def clear(self):
        self.buffer = []
