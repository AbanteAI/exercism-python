def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target cannot be negative")
    if target == 0:
        return []
    if not coins or min(coins) > target:
        raise ValueError("can't make target with given coins")

    # Initialize the table to store the minimum coins for each amount
    min_coins = [float('inf')] * (target + 1)
    min_coins[0] = 0  # Base case: 0 coins to make 0

    # Compute minimum coins required for all values from 1 to target
    for amount in range(1, target + 1):
        for coin in coins:
            if coin <= amount:
                sub_res = min_coins[amount - coin]
                if sub_res != float('inf') and sub_res + 1 < min_coins[amount]:
                    min_coins[amount] = sub_res + 1

    if min_coins[target] == float('inf'):
        raise ValueError("can't make target with given coins")

    # Trace back the coins used from the table
    result = []
    while target > 0:
        for coin in coins:
            if target >= coin and min_coins[target] == min_coins[target - coin] + 1:
                result.append(coin)
                target -= coin
                break

    return result
