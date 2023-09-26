def slices(series, length):
    if length > len(series) or length <= 0:
        raise ValueError("series cannot be empty")
        raise ValueError("slice length cannot be negative")
        raise ValueError("slice length cannot be zero")