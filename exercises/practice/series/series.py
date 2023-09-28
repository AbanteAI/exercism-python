def slices(series, length):
    if length <= 0:
        raise ValueError("Slice length cannot be zero or negative")
    if not series:
        raise ValueError("Series cannot be empty")
    if length > len(series):
        raise ValueError("Slice length cannot be greater than series length")
    
    result = []
    for i in range(len(series) - length + 1):
        result.append(series[i:i+length])
    
    return result
