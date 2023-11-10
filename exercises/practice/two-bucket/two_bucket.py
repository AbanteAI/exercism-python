def measure(bucket_one, bucket_two, goal, start_bucket):
    # Helper function to pour from one bucket to the other
    def pour(from_bucket, to_bucket, from_size, to_size):
        pour_amount = min(from_bucket, to_size - to_bucket)
        return from_bucket - pour_amount, to_bucket + pour_amount

    # Initialize buckets
    buckets = {'one': 0, 'two': 0}
    sizes = {'one': bucket_one, 'two': bucket_two}
    actions = 0

    # Determine which bucket is which
    start = 'one' if start_bucket == 'one' else 'two'
    other = 'two' if start_bucket == 'one' else 'one'

    # Start by filling the first bucket if specified
    buckets[start] = sizes[start]
    actions += 1

    # Perform actions until the goal is reached
    while goal not in buckets.values():
        if buckets[start] == 0:
            # Fill the starting bucket
            buckets[start] = sizes[start]
        elif buckets[other] == sizes[other]:
            # Empty the other bucket
            buckets[other] = 0
        else:
            # Pour from the starting bucket to the other bucket
            buckets[start], buckets[other] = pour(buckets[start], buckets[other], sizes[start], sizes[other])

        actions += 1

        # Check for the impossible situation where the goal cannot be reached
        if buckets[start] == sizes[start] and buckets[other] == 0:
            # If we're in a loop where the start bucket is full and the other is empty, the goal is not reachable
            raise ValueError("The goal cannot be reached with the given bucket sizes.")

    # Determine which bucket has the goal amount and how much is left in the other
    goal_bucket = start if buckets[start] == goal else other
    remaining = buckets[other] if goal_bucket == start else buckets[start]

    return actions, goal_bucket, remaining