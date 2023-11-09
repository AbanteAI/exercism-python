def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("cannot find change for negative value")
    if target == 0:
        return []
    if min(coins) > target:
        raise ValueError("cannot find change for value smaller than the smallest coin")

    # Initialize the table to store the minimum coins for each amount
    min_coins = [float('inf')] * (target + 1)
    min_coins[0] = 0  # Base case: 0 coins to make 0 value

    # Compute minimum coins required for all values from 1 to target
    for amount in range(1, target + 1):
        for coin in coins:
            if coin <= amount:
                sub_res = min_coins[amount - coin]
                if sub_res != float('inf') and sub_res + 1 < min_coins[amount]:
                    min_coins[amount] = sub_res + 1

    if min_coins[target] == float('inf'):
        raise ValueError("cannot make target with given coins")

    # Trace back the coins used from the min_coins table
    result = []
    while target > 0:
        for coin in coins:
            if target >= coin and min_coins[target] == min_coins[target - coin] + 1:
                result.append(coin)
                target -= coin
                break

    return result
