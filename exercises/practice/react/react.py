class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value
        self._callbacks = []
    def add_callback(self, callback):
        if callback not in self._callbacks:
            self._callbacks.append(callback)
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if self._value != new_value:
            self._value = new_value
            for callback in self._callbacks:
                callback(self._value)

    def remove_callback(self, callback):
        if callback in self._callbacks:
            self._callbacks.remove(callback)
    def add_callback(self, callback):
        if callback not in self._callbacks:
            self._callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self._callbacks:
            self._callbacks.remove(callback)

class ComputeCell:
    def __init__(self, inputs, compute_function):
        self._value = compute_function(inputs)
        self._inputs = inputs
        self._compute_function = compute_function
        self._callbacks = []
    @property
    def value(self):
        return self._value

    def recalculate(self):
        new_value = self._compute_function(self._inputs)
        if new_value != self._value:
            self._value = new_value
            for callback in self._callbacks:
                callback()

    def add_callback(self, callback):
        if callback not in self._callbacks:
            self._callbacks.append(callback)
            for input_cell in self._inputs:
                input_cell.add_compute_cell(self)

    def remove_callback(self, callback):
        if callback in self._callbacks:
            self._callbacks.remove(callback)
            for input_cell in self._inputs:
                input_cell.remove_compute_cell(self)

        # This method is now implemented above and can be removed.
    