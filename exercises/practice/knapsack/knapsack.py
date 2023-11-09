def maximum_value(maximum_weight, items):
    # Initialize a table to store the maximum value at each n and W
    n = len(items)
    dp = [[0 for x in range(maximum_weight + 1)] for x in range(n + 1)]

    # Build table dp[][] in bottom up manner
    for i in range(n + 1):
        for w in range(maximum_weight + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif items[i-1]['weight'] <= w:
                dp[i][w] = max(items[i-1]['value'] + dp[i-1][w-items[i-1]['weight']], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][maximum_weight]
