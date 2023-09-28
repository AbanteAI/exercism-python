def find(search_list, value):
    left, right = 0, len(search_list) - 1

    while left <= right:
        middle = (left + right) // 2

        if search_list[middle] == value:
            return middle
        elif search_list[middle] < value:
            left = middle + 1
        else:
            right = middle - 1

    raise ValueError("value not in array")