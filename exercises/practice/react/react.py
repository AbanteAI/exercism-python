class InputCell:
    def __init__(self, initial_value):
        self.value = initial_value
        self.callbacks = []

    def set_value(self, new_value):
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
    def notify_callbacks(self):
        for callback in self.callbacks:
            callback()
    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        self.callbacks.remove(callback)
class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self.value = self.compute_value()
        self.callbacks = []

        for input_cell in inputs:
            input_cell.add_callback(self.update_value)

    def compute_value(self):
    def update_value(self):
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()

    def notify_callbacks(self):
        for callback in self.callbacks:
            callback()

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        self.callbacks.remove(callback)