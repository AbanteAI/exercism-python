def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []
    for l in lists:
        result.extend(l)
    return result


def filter(function, lst):
    return [x for x in lst if function(x)]


def length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count


def map(function, lst):
    return [function(x) for x in lst]


def foldl(function, lst, initial):
    result = initial
    for x in lst:
        result = function(result, x)
    return result


def foldr(function, lst, initial):
    result = initial
    for x in reversed(lst):
        result = function(x, result)
    return result


def reverse(lst):
    return lst[::-1]
