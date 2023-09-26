def maximum_value(maximum_weight, items):
    weights = [item["weight"] for item in items]
    values = [item["value"] for item in items]

    n = len(items)
    dp = [[0] * (maximum_weight + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]
        for w in range(maximum_weight + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][maximum_weight]
