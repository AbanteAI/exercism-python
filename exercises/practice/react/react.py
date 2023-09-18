class InputCell:
    def __init__(self, initial_value):
        self.value = initial_value

        self.callbacks = []

    def add_callback(self, callback):
        self.callbacks.append(callback)
    def set_value(self, new_value):
        self.value = new_value
        # Add propagation logic here

class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.value = compute_function(*(cell.value for cell in inputs))

        self.inputs = inputs
        self.compute_function = compute_function
        self.callbacks = set()

        for input_cell in inputs:
            input_cell.add_callback(self.update)

    def update(self):
        new_value = self.compute_function(*(cell.value for cell in self.inputs))
        if new_value != self.value:
            self.value = new_value
            for callback in self.callbacks:
                callback(self)

    def add_callback(self, callback):
        self.callbacks.add(callback)

    def remove_callback(self, callback):
        self.callbacks.discard(callback)
    def add_callback(self, callback):
        pass

    def remove_callback(self, callback):
        pass
    