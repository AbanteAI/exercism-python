def maximum_value(maximum_weight, items):
    # Initialize a list to store the maximum value at each weight from 0 to maximum_weight
    dp = [0] * (maximum_weight + 1)

    # Iterate over each item and update the dp list accordingly
    for item in items:
        weight = item["weight"]
        value = item["value"]
        # Traverse the dp list in reverse to avoid using an item more than once
        for w in range(maximum_weight, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    # The last element of dp will hold the maximum value
    return dp[maximum_weight]