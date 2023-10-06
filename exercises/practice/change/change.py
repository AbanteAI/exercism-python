def find_fewest_coins(coins, target):
    if target < 0 or (coins and target < min(coins)):
        raise ValueError("Invalid target value")

    coins.sort(reverse=True)
    result = []

    def helper(remaining, coin_idx, coins_so_far):
        nonlocal result

        if remaining == 0:
            if not result or len(coins_so_far) < len(result):
                result = coins_so_far
            return

        if coin_idx >= len(coins) or remaining < coins[coin_idx]:
            return

        max_coin_qty = remaining // coins[coin_idx]
        for qty in range(max_coin_qty, -1, -1):
            if not result or len(coins_so_far) + qty < len(result):
                helper(remaining - coins[coin_idx] * qty, coin_idx + 1, coins_so_far + [coins[coin_idx]] * qty)

    helper(target, 0, [])
    if not result:
        raise ValueError("Can't make target with given coins")

    return result
