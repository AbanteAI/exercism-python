def measure(bucket_one, bucket_two, goal, start_bucket):
    # Initialize buckets
    buckets = {'one': 0, 'two': 0}
    bucket_sizes = {'one': bucket_one, 'two': bucket_two}
    actions = 0

    # Determine which bucket is which
    fill_first, fill_second = ('one', 'two') if start_bucket == 'one' else ('two', 'one')

    # Helper function to fill a bucket
    def fill(bucket):
        nonlocal actions
        buckets[bucket] = bucket_sizes[bucket]
        actions += 1

    # Helper function to empty a bucket
    def empty(bucket):
        nonlocal actions
        buckets[bucket] = 0
        actions += 1

    # Helper function to pour from one bucket to the other
    def pour(from_bucket, to_bucket):
        nonlocal actions
        amount = min(buckets[from_bucket], bucket_sizes[to_bucket] - buckets[to_bucket])
        buckets[from_bucket] -= amount
        buckets[to_bucket] += amount
        actions += 1

    # Fill the first bucket
    fill(fill_first)

    # Main loop to perform actions until the goal is reached
    while not (goal in buckets.values()):
        if buckets[fill_first] == goal or buckets[fill_second] == goal:
            break
        if buckets[fill_first] == 0:
            fill(fill_first)
        elif buckets[fill_second] == bucket_sizes[fill_second]:
            empty(fill_second)
        elif buckets[fill_first] != 0 and buckets[fill_second] != bucket_sizes[fill_second]:
            pour(fill_first, fill_second)
        else:
            raise ValueError("Cannot reach the desired goal with the given bucket sizes.")

        # Check for impossible situation
        if buckets[fill_first] == 0 and buckets[fill_second] == bucket_sizes[fill_second]:
            raise ValueError("Cannot reach the desired goal with the given bucket sizes.")

    # Determine which bucket has the goal amount and how much is in the other bucket
    goal_bucket = 'one' if buckets['one'] == goal else 'two'
    other_bucket = 'two' if goal_bucket == 'one' else 'one'
    remaining = buckets[other_bucket]

    return actions, goal_bucket, remaining