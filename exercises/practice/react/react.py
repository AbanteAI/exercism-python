class InputCell:
    def __init__(self, initial_value):
        self.value = initial_value
        self.callbacks = []


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self.callbacks = []
        self._value = compute_function(*[input_cell.value for input_cell in inputs])
        self._previous_value = None
    def recompute(self):
        new_value = self.compute_function(*[input_cell.value for input_cell in self.inputs])
        if new_value != self._value:
            self._value = new_value
            for callback in self.callbacks:
                callback(self._value)

    def add_callback(self, callback):
        if callback not in self.callbacks:
            self.callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self.callbacks:
            self.callbacks.remove(callback)
    