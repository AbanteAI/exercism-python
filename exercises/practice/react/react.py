class InputCell:
    def __init__(self, initial_value):
        self.value = initial_value
        self.observers = []

    def _notify(self):
        for observer in self.observers:
            observer()

    def set_value(self, new_value):
        if self.value != new_value:
            self.value = new_value
            self._notify()

class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self.value = self.compute_function([input_cell.value for input_cell in self.inputs])
        self.callbacks = []

        for input_cell in self.inputs:
            input_cell.observers.append(self.recompute)

    def recompute(self):
        new_value = self.compute_function([input_cell.value for input_cell in self.inputs])
        if new_value != self.value:
            self.value = new_value
            for callback in self.callbacks:
                callback(self.value)
    def add_callback(self, callback):
        if callback not in self.callbacks:
            self.callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self.callbacks:
            self.callbacks.remove(callback)
    