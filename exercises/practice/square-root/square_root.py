def square_root(number):
    if number < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    
    if number == 0 or number == 1:
        return number
    
    # Use binary search method
    start, end = 0, number
    while start <= end:
        mid = (start + end) // 2
        mid_squared = mid * mid

        if mid_squared == number:
            return mid
        elif mid_squared < number:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    
    return result
