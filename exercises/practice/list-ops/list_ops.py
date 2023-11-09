def append(list1, list2):
    for item in list2:
        list1.append(item)
    return list1


def concat(lists):
    result = []
    for list in lists:
        result = append(result, list)
    return result


def filter(function, list):
    filtered_list = []
    for item in list:
        if function(item):
            filtered_list.append(item)
    return filtered_list


def length(list):
    count = 0
    for _ in list:
        count += 1
    return count


def map(function, list):
    mapped_list = []
    for item in list:
        mapped_list.append(function(item))
    return mapped_list


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
    reversed_list = []
    for item in list:
        reversed_list.insert(0, item)
    return reversed_list
