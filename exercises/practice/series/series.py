def slices(series, length):
    if length <= 0:
        raise ValueError("slice length cannot be negative")
        raise ValueError("series cannot be empty")
        raise ValueError("slice length cannot be greater than series length")
    return [series[i:i+length] for i in range(len(series)-length+1)]
