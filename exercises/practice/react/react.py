class InputCell:
    def __init__(self, initial_value):
        self.value = initial_value

    def set_value(self, new_value):
        self.value = new_value
        for input_cell in self.inputs:
            if isinstance(input_cell, ComputeCell):
                input_cell.update_value()

class ComputeCell:
        self.value = None
        self.inputs = inputs
        self.compute_function = compute_function
        self.callbacks = []
        self.update_value()
        self.compute_function = compute_function
        self.callbacks = []
        self.update_value()

        if callback not in self.callbacks:
            self.callbacks.append(callback)

        if callback in self.callbacks:
            self.callbacks.remove(callback)
    
    def update_value(self):
        new_value = self.compute_function([input_cell.value for input_cell in self.inputs])
        if new_value != self.value:
            self.value = new_value
            for callback in self.callbacks:
                callback(self.value)
            for input_cell in self.inputs:
                if isinstance(input_cell, ComputeCell):
                    input_cell.update_value()