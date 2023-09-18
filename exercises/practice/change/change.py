def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")

    dp = [0] + [float('inf')] * target
    coins_used = [0] + [None] * target

    for coin in coins:
        for i in range(coin, target + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coins_used[i] = coin

    if dp[target] == float('inf'):
        raise ValueError("No combination of coins can sum to the target value")

    result = []
    while target > 0:
        result.append(coins_used[target])
        target -= coins_used[target]

    return sorted(result)