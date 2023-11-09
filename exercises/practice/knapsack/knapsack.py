def maximum_value(maximum_weight, items):
    # Initialize a list for dynamic programming
    dp = [0] * (maximum_weight + 1)

    # Iterate over each item
    for item in items:
        weight = item['weight']
        value = item['value']

        # Traverse the dp array from the maximum_weight down to weight
        for j in range(maximum_weight, weight - 1, -1):
            # If adding the item's value yields a better solution, update dp[j]
            dp[j] = max(dp[j], dp[j - weight] + value)

    # The last element of dp will be the maximum value achievable
    return dp[maximum_weight]
