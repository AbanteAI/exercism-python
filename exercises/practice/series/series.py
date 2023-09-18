def slices(series, length):
    if length <= 0:
        raise ValueError("slice length cannot be negative" if length < 0 else "slice length cannot be zero")
    if length > len(series):
        raise ValueError("series cannot be empty" if len(series) == 0 else "slice length cannot be greater than series length")

    return [series[i:i+length] for i in range(len(series) - length + 1)]