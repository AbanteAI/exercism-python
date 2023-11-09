def measure(bucket_one, bucket_two, goal, start_bucket):
    def fill(bucket):
        return bucket

    def empty(bucket):
        return 0

    def pour(from_bucket, to_bucket, to_bucket_size):
        transfer = min(from_bucket, to_bucket_size - to_bucket)
        return from_bucket - transfer, to_bucket + transfer

    buckets = {'one': 0, 'two': 0}
    bucket_sizes = {'one': bucket_one, 'two': bucket_two}
    actions = 0

    if start_bucket == 'one':
        first, second = 'one', 'two'
    else:
        first, second = 'two', 'one'

    while True:
        if buckets[first] == goal:
            return actions, first, buckets[second]
        if buckets[second] == goal:
            return actions, second, buckets[first]

        if buckets[first] == 0:
            buckets[first] = fill(bucket_sizes[first])
            actions += 1
        elif buckets[second] == bucket_sizes[second]:
            buckets[second] = empty(bucket_sizes[second])
            actions += 1
        else:
            buckets[first], buckets[second] = pour(buckets[first], buckets[second], bucket_sizes[second])
            actions += 1

        if buckets[first] == bucket_sizes[first] and buckets[second] == 0:
            # This state is not allowed, so we pour the water back and continue with the next action
            buckets[first], buckets[second] = pour(buckets[first], buckets[second], bucket_sizes[second])

        if actions > max(bucket_sizes['one'], bucket_sizes['two']) * 2:
            raise ValueError("Cannot reach the desired goal with the given buckets.")