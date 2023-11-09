def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("cannot find change for negative value")
    if target == 0:
        return []
    if not coins or min(coins) > target:
        raise ValueError("no coins available to make change")

    # Initialize the table to store the minimum coins for each amount
    min_coins = [0] + [float('inf')] * target

    # Build the table in a bottom-up manner
    for coin in coins:
        for amount in range(coin, target + 1):
            if min_coins[amount - coin] != float('inf'):
                min_coins[amount] = min(min_coins[amount], min_coins[amount - coin] + 1)

    if min_coins[target] == float('inf'):
        raise ValueError("can't make target with given coins")

    # Trace back the coins used
    change = []
    while target > 0:
        for coin in reversed(coins):
            if min_coins[target - coin] == min_coins[target] - 1:
                change.append(coin)
                target -= coin
                break

    return change
