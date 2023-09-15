class InputCell:
    def __init__(self, initial_value):
        self.value = None

class InputCell:
        self.value = initial_value

class ComputeCell:
    def __init__(self, inputs, compute_function):
    def update(self, inputs):
        new_value = self.compute_function(inputs)
        if new_value != self.value:
            self.value = new_value
            for callback in self.callbacks:
                callback()

    def add_callback(self, callback):
        if callback not in self.callbacks:
            self.callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self.callbacks:
            self.callbacks.remove(callback)
    