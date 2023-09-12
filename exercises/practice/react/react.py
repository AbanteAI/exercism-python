class InputCell:
    def __init__(self, initial_value):
        self.value = initial_value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        self._notify_dependents()


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self.callbacks = []
        self.dependents = []
        self.value = self.compute_function([input.value for input in self.inputs])

    def _update_value(self):
        new_value = self.compute_function([input.value for input in self.inputs])
        if new_value != self.value:
            self.value = new_value
            self._notify_dependents()

    def _notify_dependents(self):
        for dependent in self.dependents:
            dependent._update_value()
        for callback in self.callbacks:
            callback(self.value)
    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        self.callbacks.remove(callback)
    