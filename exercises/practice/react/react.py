class InputCell:
    def __init__(self, initial_value):
        self.value = initial_value

    def set_value(self, new_value):
        self.value = new_value

    def get_value(self):
        return self.value

class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self.callbacks = []
        self.update_value()

    def update_value(self):
        new_value = self.compute_function(*[input_cell.get_value() for input_cell in self.inputs])
        if new_value != self.value:
            self.value = new_value
            for callback in self.callbacks:
                callback(self.value)

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        self.callbacks.remove(callback)
    def add_callback(self, callback):
        pass

    def remove_callback(self, callback):
        pass
    