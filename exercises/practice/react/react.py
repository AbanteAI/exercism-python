class InputCell:
    def __init__(self, initial_value):
        self.value = initial_value


    def set_value(self, new_value):
        self.value = new_value
        self.notify_dependents()
        
    def notify_dependents(self):
        for dependent in self.dependents:
            dependent.recompute()
class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.value = compute_function(*[input_cell.value for input_cell in inputs])

    def recompute(self):
        old_value = self.value
        self.value = self.compute_function(*[input_cell.value for input_cell in self.inputs])
        if old_value != self.value:
            self.notify_callbacks()
            for dependent in self.dependents:
                dependent.recompute()

    def add_dependent(self, dependent):
        self.dependents.append(dependent)

    def remove_dependent(self, dependent):
        self.dependents.remove(dependent)
    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        self.callbacks.remove(callback)
    