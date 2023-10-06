def maximum_value(maximum_weight, items):
    n = len(items)
    dp = [[0] * (maximum_weight + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_weight = items[i - 1]["weight"]
        item_value = items[i - 1]["value"]
        for w in range(maximum_weight + 1):
            if item_weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_weight] + item_value)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][maximum_weight]