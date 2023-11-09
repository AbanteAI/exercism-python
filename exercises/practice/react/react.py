class InputCell:
    def __init__(self, initial_value):
        self.value = initial_value
    @property
    def value(self):
        return self._value

    @value.setter
    @value.setter
    def value(self, new_value):
        if new_value != self._value:
            self._value = new_value
            self._propagate()


    def _propagate(self):
        for cell in ComputeCell._registry:
            if self in cell.inputs:
                cell._compute_value()
class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.value = None
        self._value = None
        self.inputs = inputs
        self.compute_function = compute_function
        self.callbacks = []
        self._compute_value()

    def _compute_value(self):
        new_value = self.compute_function(*[input_cell.value for input_cell in self.inputs])
        if new_value != self._value:
            old_value = self._value
            self._value = new_value
            if old_value is not None:
                self._trigger_callbacks()

    def _trigger_callbacks(self):
        for callback in self.callbacks:
            callback(self._value)

    def add_callback(self, callback):
        if callback not in self.callbacks:
            self.callbacks.append(callback)
        return self._value

    _registry = []

    def __init__(self, inputs, compute_function):
        ComputeCell._registry.append(self)
        # ... existing code ...

    def remove_callback(self, callback):
        if callback in self.callbacks:
            self.callbacks.remove(callback)
        ComputeCell._registry.remove(self)
    