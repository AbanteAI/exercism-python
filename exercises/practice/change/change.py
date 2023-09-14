def find_fewest_coins(coins, target):
    pass
def find_fewest_coins_helper(coins, target, memo):
    if target == 0:
        return []
    if target < 0:
        return None
    if target in memo:
        return memo[target]

    min_coins = None
    for coin in coins:
        remaining_target = target - coin
        coins_list = find_fewest_coins_helper(coins, remaining_target, memo)
        if coins_list is not None:
            coins_list = coins_list + [coin]
            if min_coins is None or len(coins_list) < len(min_coins):
                min_coins = coins_list
    memo[target] = min_coins
    return min_coins

def find_fewest_coins(coins, target):
    memo = {}
    result = find_fewest_coins_helper(coins, target, memo)
    return sorted(result) if result is not None else -1
