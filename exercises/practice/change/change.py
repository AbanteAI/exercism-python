def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("Target amount cannot be negative.")
    if target < min(coins):
        raise ValueError("Target amount is smaller than the smallest coin value.")
    if target == 0:
        return []
    if target in coins:
        return [target]
    
    coins.sort(reverse=True)
    num_coins = []
    for coin in coins:
        while target >= coin:
            target -= coin
            num_coins.append(coin)
    if target > 0:
        raise ValueError("Cannot make target amount with given coins.")
    return num_coins
    if target < 0:
        raise ValueError("Target amount cannot be negative.")
    if target < min(coins):
        raise ValueError("Target amount is smaller than the smallest coin value.")
    if target == 0:
        return []
    if target in coins:
        return [target]
    
    coins.sort(reverse=True)
    num_coins = []
    for coin in coins:
        while target >= coin:
            target -= coin
            num_coins.append(coin)
    if target > 0:
        raise ValueError("Cannot make target amount with given coins.")
    return num_coins
        raise ValueError("Target amount cannot be negative.")
    if target < min(coins):
        raise ValueError("Target amount is smaller than the smallest coin value.")
    if target == 0:
        return []
    if target in coins:
        return [target]
    
    coins.sort(reverse=True)
    num_coins = []
    for coin in coins:
        while target >= coin:
            target -= coin
            num_coins.append(coin)
    if target > 0:
        raise ValueError("Cannot make target amount with given coins.")
    return num_coins
