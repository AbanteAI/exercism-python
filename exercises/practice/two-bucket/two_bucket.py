def measure(bucket_one, bucket_two, goal, start_bucket):
    # Helper function to pour from one bucket to the other
    def pour(from_bucket, to_bucket, to_bucket_size):
        transfer = min(from_bucket, to_bucket_size - to_bucket)
        return from_bucket - transfer, to_bucket + transfer

    # Initialize buckets
    buckets = {'one': 0, 'two': 0}
    bucket_sizes = {'one': bucket_one, 'two': bucket_two}
    actions = 0

    # Determine the order of filling buckets
    first, second = ('one', 'two') if start_bucket == 'one' else ('two', 'one')

    # Start measuring
    while True:
        # Check if we have reached the goal in either bucket
        if buckets[first] == goal or buckets[second] == goal:
            goal_bucket = first if buckets[first] == goal else second
            other_bucket = second if goal_bucket == first else first
            return (actions, goal_bucket, buckets[other_bucket])

        if buckets[first] == 0:
            buckets[first] = bucket_sizes[first]
            actions += 1
        elif buckets[second] == bucket_sizes[second]:
            buckets[second] = 0
            actions += 1
        else:
            buckets[first], buckets[second] = pour(buckets[first], buckets[second], bucket_sizes[second])
            actions += 1

        # Check for impossible situation
        if buckets[first] == bucket_sizes[first] and buckets[second] == 0:
            raise ValueError("Cannot reach the goal with the given bucket sizes and starting bucket.")