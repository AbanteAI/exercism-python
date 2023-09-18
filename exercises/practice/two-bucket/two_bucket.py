def measure(bucket_one, bucket_two, goal, start_bucket):
    def pour(src, dest):
        transfer = min(src[1], dest[0] - dest[1])
        src[1] -= transfer
        dest[1] += transfer
        return 1

    def empty(bucket):
        bucket[1] = 0
        return 1

    def fill(bucket):
        bucket[1] = bucket[0]
        return 1

    buckets = [[bucket_one, 0], [bucket_two, 0]]
    start_bucket_idx = 0 if start_bucket == 'one' else 1
    other_bucket_idx = 1 - start_bucket_idx

    actions = fill(buckets[start_bucket_idx])
    while goal not in (buckets[0][1], buckets[1][1]):
        if buckets[start_bucket_idx][1] == 0:
            actions += fill(buckets[start_bucket_idx])
        elif buckets[other_bucket_idx][1] == buckets[other_bucket_idx][0]:
            actions += empty(buckets[other_bucket_idx])
        else:
            actions += pour(buckets[start_bucket_idx], buckets[other_bucket_idx])

    goal_bucket = 'one' if buckets[0][1] == goal else 'two'
    other_bucket_liters = buckets[other_bucket_idx][1]

    return actions, goal_bucket, other_bucket_liters