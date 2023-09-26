class InputCell:
    def __init__(self, initial_value):
        self.value = initial_value

    def set_value(self, new_value):
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()

    def get_value(self):
        return self.value

    def notify_callbacks(self):
        for callback in self.callbacks:
            callback(self)

class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self.value = self.compute_value()
        self.callbacks = []

    def get_value(self):
        return self.value

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        self.callbacks.remove(callback)

    def compute_value(self):
        return self.compute_function([input.get_value() for input in self.inputs])

    def notify_callbacks(self):
        for callback in self.callbacks:
            callback(self)
        for input in self.inputs:
            input.add_callback(self.recompute_value)
    def add_callback(self, callback):
        pass

    def remove_callback(self, callback):
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        for input in self.inputs:
            input.remove_callback(self.recompute_value)
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        for input in self.inputs:
            input.remove_callback(self.recompute_value)
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        for input in self.inputs:
            input.remove_callback(self.recompute_value)
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        for input in self.inputs:
            input.remove_callback(self.recompute_value)
        for input in self.inputs:
            input.remove_callback(self.recompute_value)
        for input in self.inputs:
            input.remove_callback(self.recompute_value)
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        for input in self.inputs:
            input.remove_callback(self.recompute_value)
        for input in self.inputs:
            input.remove_callback(self.recompute_value)
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        for input in self.inputs:
            input.remove_callback(self.recompute_value)
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        for input in self.inputs:
            input.remove_callback(self.recompute_value)
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        for input in self.inputs:
            input.remove_callback(self.recompute_value)
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        new_value = self.compute_value()
        if self.value != new_value:
            self.value = new_value
            self.notify_callbacks()
        pass
    