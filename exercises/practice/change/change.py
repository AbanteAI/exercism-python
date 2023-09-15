def find_fewest_coins(coins, target):
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        while target >= coin:
            result.append(coin)
            target -= coin
    return result