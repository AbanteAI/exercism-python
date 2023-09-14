from typing import Callable, List
class InputCell:
    def __init__(self, initial_value):
        self.value = None
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.value = None
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

        self.inputs = inputs
        self.compute_function = compute_function
        self.value = self.compute_function([input.value for input in self.inputs])
        self.callbacks = set()
    def add_callback(self, callback):
        pass
        self.callbacks.add(callback)

    def remove_callback(self, callback):
        self.callbacks.remove(callback)
        pass
    