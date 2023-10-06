def append(list1, list2):
    return list1 + list2

def concatenate(lists):
def concatenate(lists):
    for sublist in lists:
        result.extend(sublist)
    return result

def filter(function, list):
    return [item for item in list if function(item)]

def length(list):
    count = 0
    for item in list:
        count += 1
    return count

def map(function, list):
    return [function(item) for item in list]

def foldl(function, list, initial):
    result = initial
    for item in list:
        result = function(result, item)
    return result

def foldr(function, list, initial):
    result = initial
    for item in reversed(list):
        result = function(item, result)
    return result

def reverse(list):
    return list[::-1]