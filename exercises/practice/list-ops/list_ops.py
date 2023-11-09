def append(list1, list2):
    for item in list2:
        list1.append(item)
    return list1

def concat(lists):
    result = []
    for lst in lists:
        result = append(result, lst)
    return result

def filter(function, list):
    return [item for item in list if function(item)]

def length(list):
    count = 0
    for _ in list:
        count += 1
    return count

def map(function, list):
    return [function(item) for item in list]

def foldl(function, list, initial):
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator

def foldr(function, list, initial):
    accumulator = initial
    for item in reversed(list):
        accumulator = function(item, accumulator)
    return accumulator

def reverse(list):
    return list[::-1]
