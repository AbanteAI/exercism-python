def slices(series, length):
    if length <= 0:
        raise ValueError("Length must be a positive integer.")
    if len(series) < length:
        raise ValueError("Series length is less than the specified length.")
    
    result = []
    for i in range(len(series) - length + 1):
        result.append(series[i:i+length])
    
    return result
