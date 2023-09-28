class InputCell:
    def __init__(self, initial_value):
        self.value = None
        self.set_value(initial_value)

    def set_value(self, new_value):
        if self.value != new_value:
            self.value = new_value
            self.value = new_value
            for dependent in self.dependents:
                dependent.recompute()
                for callback in dependent.callbacks:
                    callback(dependent.value)


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self.callbacks = []
        self.value = self.compute_value()

        for input_cell in inputs:
            input_cell.dependents.append(self)

    def compute_value(self):
        return self.compute_function([input.value for input in self.inputs])

    def recompute(self):
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            for callback in self.callbacks:
                callback(self.value)
            for dependent in self.dependents:
                dependent.recompute()
    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        self.callbacks.remove(callback)
    