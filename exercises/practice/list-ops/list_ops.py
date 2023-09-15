def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []
    for lst in lists:
        result += lst
    return result


def filter(function, lst):
    return [item for item in lst if function(item)]


def length(lst):
    return len(lst)


def map(function, lst):
    return [function(item) for item in lst]


def foldl(function, lst, initial):
    result = initial
    for item in lst:
        result = function(result, item)
    return result


def foldr(function, lst, initial):
    result = initial
    for item in reversed(lst):
        result = function(item, result)
    return result


def reverse(lst):
    return lst[::-1]