class InputCell:
        self.value = initial_value


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self.value = None
        self.callbacks = []

        for input_cell in inputs:
            input_cell.add_callback(self.update_value)

        self.update_value()

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        self.callbacks.remove(callback)

        new_value = self.compute_function([input_cell.value if input_cell.value is not None else None for input_cell in self.inputs])

        if new_value is not None and new_value != self.value:
            self.value = new_value
            for callback in self.callbacks:
                callback(self.value)
    def __init__(self, inputs, compute_function):
        self.value = None

    def add_callback(self, callback):
        pass

    def remove_callback(self, callback):
        pass
    