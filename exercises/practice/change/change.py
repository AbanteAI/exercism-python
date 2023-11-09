def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("cannot find change for negative value")
    if target == 0:
        return []
    if min(coins) > target:
        raise ValueError("cannot find change for value smaller than the smallest coin value")

    # Initialize a list to store the minimum coins needed for each amount
    min_coins = [0] + [float('inf')] * target

    # Build the list from the smallest value up to the target value
    for coin in coins:
        for amount in range(coin, target + 1):
            if min_coins[amount - coin] + 1 < min_coins[amount]:
                min_coins[amount] = min_coins[amount - coin] + 1

    # If the target value is still set to infinity, no change can be made
    if min_coins[target] == float('inf'):
        raise ValueError("can't make target with given coins")

    # Trace back the coins used to find the minimum number of coins
    result = []
    while target > 0:
        for coin in coins:
            if target >= coin and min_coins[target] == min_coins[target - coin] + 1:
                result.append(coin)
                target -= coin
                break

    return result
