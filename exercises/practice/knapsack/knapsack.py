def maximum_value(maximum_weight, items):
    # Initialize a table to store the maximum value at each n items and at each capacity
    n = len(items)
    dp = [[0 for x in range(maximum_weight + 1)] for x in range(n + 1)]

    # Build table dp[][] in bottom up manner
    for i in range(n + 1):
        for w in range(maximum_weight + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif items[i-1]['weight'] <= w:
                # If including the item is beneficial
                dp[i][w] = max(items[i-1]['value'] + dp[i-1][w-items[i-1]['weight']], dp[i-1][w])
            else:
                # If not including the item
                dp[i][w] = dp[i-1][w]

    # The maximum value that can be obtained with the given weight limit is found at dp[n][maximum_weight]
    return dp[n][maximum_weight]
