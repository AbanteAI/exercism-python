def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    if target != 0 and min(coins) > target:
        raise ValueError("Target value is smaller than the smallest coin value")

    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    coin_list = [None] * (target + 1)

    for coin in coins:
        for i in range(coin, target + 1):
            if dp[i] > dp[i - coin] + 1:
                dp[i] = dp[i - coin] + 1
                coin_list[i] = coin

    if dp[target] == float('inf'):
        raise ValueError("can't make target with given coins")

    result = []
    while target > 0:
        result.append(coin_list[target])
        target -= coin_list[target]

    return sorted(result)