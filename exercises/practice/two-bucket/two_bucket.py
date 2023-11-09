def measure(bucket_one, bucket_two, goal, start_bucket):
    def fill(bucket):
        return bucket

    def empty(bucket):
        return 0

    def pour(from_bucket, to_bucket, to_bucket_size):
        transfer = min(from_bucket, to_bucket_size - to_bucket)
        return from_bucket - transfer, to_bucket + transfer

    bucket_sizes = {'one': bucket_one, 'two': bucket_two}
    buckets = {'one': 0, 'two': 0}
    actions = 0

    if start_bucket not in bucket_sizes:
        raise ValueError("Invalid start bucket name.")

    current_bucket = start_bucket
    other_bucket = 'two' if current_bucket == 'one' else 'one'

    while True:
        if buckets[current_bucket] == goal or buckets[other_bucket] == goal:
            goal_bucket = current_bucket if buckets[current_bucket] == goal else other_bucket
            other_bucket = 'two' if goal_bucket == 'one' else 'one'
            return (actions, goal_bucket, buckets[other_bucket])

        if buckets[current_bucket] < bucket_sizes[current_bucket]:
            buckets[current_bucket] = fill(bucket_sizes[current_bucket])
            actions += 1
        elif buckets[other_bucket] > 0:
            buckets[current_bucket], buckets[other_bucket] = pour(
                buckets[other_bucket], buckets[current_bucket], bucket_sizes[current_bucket])
            actions += 1

        if buckets[current_bucket] == goal or buckets[other_bucket] == goal:
            goal_bucket = current_bucket if buckets[current_bucket] == goal else other_bucket
            other_bucket = 'two' if goal_bucket == 'one' else 'one'
            return (actions, goal_bucket, buckets[other_bucket])

        if buckets[current_bucket] == bucket_sizes[current_bucket] and buckets[other_bucket] == 0:
            buckets[other_bucket] = fill(bucket_sizes[other_bucket])
            actions += 1
        elif buckets[current_bucket] > 0 and buckets[other_bucket] < bucket_sizes[other_bucket]:
            buckets[current_bucket], buckets[other_bucket] = pour(
                buckets[current_bucket], buckets[other_bucket], bucket_sizes[other_bucket])
            actions += 1

        if actions > max(bucket_sizes.values()) * 2:
            raise ValueError("No solution possible with the given parameters.")
