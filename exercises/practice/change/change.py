def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("Cannot find change for negative values")

    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[target] == float('inf'):
        raise ValueError("No combination of coins can add up to the target")

    result = []
    while target > 0:
        for coin in coins:
            if dp[target - coin] == dp[target] - 1:
                result.append(coin)
                target -= coin
                break

    return result