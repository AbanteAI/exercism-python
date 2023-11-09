class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value
        self._callbacks = []
    @property
    def value(self):
        return self._value



class ComputeCell:
    def __init__(self, inputs, compute_function):
        self._inputs = inputs
        self._compute_function = compute_function
        self._callbacks = []
        self._value = self._compute_function(*[input_cell.value for input_cell in self._inputs])
        self._prev_value = None
        for input_cell in self._inputs:
            input_cell._callbacks.append(self._recompute)
        self._recompute(None)  # Initialize the value
        self._inputs = inputs
        self._compute_function = compute_function
        self._callbacks = []
        self._value = self._compute_function(*[input_cell.value for input_cell in self._inputs])
        self._prev_value = None
        for input_cell in self._inputs:
            input_cell._callbacks.append(self._recompute)

    def _recompute(self, _):
        new_value = self._compute_function(*[input_cell.value for input_cell in self._inputs])
        if new_value != self._value:
            self._prev_value = self._value
            self._value = new_value
            if self._prev_value != self._value:
                for callback in self._callbacks:
                    callback(self._value)

    @property
    def value(self):
        return self._value

        self._callbacks.append(callback)

        if callback in self._callbacks:
            self._callbacks.remove(callback)
    