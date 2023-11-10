def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target cannot be negative")
    if target == 0:
        return []
    if not coins or min(coins) > target:
        raise ValueError("can't make target with given coins")

    # Initialize the table to store the minimum coins for each amount
    min_coins = [0] + [float('inf')] * target

    # Build the table in a bottom-up manner
    for coin in coins:
        for amount in range(coin, target + 1):
            if min_coins[amount - coin] != float('inf'):
                min_coins[amount] = min(min_coins[amount], min_coins[amount - coin] + 1)

    if min_coins[target] == float('inf'):
        raise ValueError("can't make target with given coins")

    # Trace back the solution
    result = []
    while target > 0:
        for coin in coins:
            if target >= coin and min_coins[target] == min_coins[target - coin] + 1:
                result.append(coin)
                target -= coin
                break

    return result