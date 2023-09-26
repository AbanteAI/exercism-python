def slices(series, length):
    if length > len(series) or length <= 0:
        raise ValueError("slice length cannot be negative" if length <= 0 else "series cannot be empty")
        raise ValueError("Invalid length")

        return [series[i:i+length] for i in range(len(series) - length + 1)]
