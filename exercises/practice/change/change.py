def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("Negative change is not allowed.")
    if target < min(coins):
        raise ValueError("Change value is smaller than the smallest coin value.")
    
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    
    for i in range(1, target + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    if dp[target] == float('inf'):
        raise ValueError("Cannot make change with the given set of coins.")
    
    result = []
    current = target
    while current > 0:
        for coin in coins:
            if coin <= current and dp[current] == dp[current - coin] + 1:
                result.append(coin)
                current -= coin
                break
    
    return result
