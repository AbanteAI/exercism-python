def accumulate(collection, operation):
    result = []
    for element in collection:
        result.append(operation(element))
    return result