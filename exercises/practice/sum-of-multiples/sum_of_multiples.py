def sum_of_multiples(limit, multiples):
    """
    Calculate the sum of all unique multiples of a given set of numbers that are less than the specified limit.
    
    :param limit: The upper bound to consider for multiples.
    :param multiples: A list of numbers for which to find multiples.
    :return: The sum of all unique multiples of the numbers in `multiples` that are less than `limit`.
    """
    # Generate sets of multiples for each number in the list, filtering out multiples that are greater than or equal to the limit.
    sets_of_multiples = (set(range(multiple, limit, multiple)) for multiple in multiples if multiple > 0)
    
    # Combine all sets into one, removing duplicates in the process.
    all_unique_multiples = set().union(*sets_of_multiples)
    
    # Return the sum of the combined set of unique multiples.
    return sum(all_unique_multiples)
