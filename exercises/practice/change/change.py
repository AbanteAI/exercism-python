def find_fewest_coins(coins, target):
    if target < 0:
    if target < 0:
        raise ValueError("target can't be negative")
    if target < min(coins):
        raise ValueError("Change value is smaller than the smallest coin value")

    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[target] == float('inf'):
        raise ValueError("Cannot make target with given coins")

    return sorted(result, reverse=True)
    i = target
    while i > 0:
        for coin in coins:
            if i >= coin and dp[i] == dp[i - coin] + 1:
                result.append(coin)
                i -= coin
                break

    return result[::-1]