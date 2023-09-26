def measure(bucket_one, bucket_two, goal, start_bucket):
    start_bucket = int(start_bucket)
    buckets = [bucket_one, bucket_two]
    actions = 1
    current_buckets = [0, 0]
    current_buckets[start_bucket - 1] = buckets[start_bucket - 1]
    while True:
        other_bucket = 1 - start_bucket
        if current_buckets[start_bucket - 1] == goal:
            return actions, start_bucket, current_buckets[other_bucket]
        if current_buckets[other_bucket] == goal:
            return actions, other_bucket + 1, current_buckets[start_bucket - 1]
        if current_buckets[start_bucket - 1] == 0:
            current_buckets[start_bucket - 1] = buckets[start_bucket - 1]
            actions += 1
        elif current_buckets[other_bucket] == buckets[other_bucket]:
            current_buckets[other_bucket] = 0
            actions += 1
        else:
            amount = min(current_buckets[start_bucket - 1], buckets[other_bucket] - current_buckets[other_bucket])
            current_buckets[start_bucket - 1] -= amount
            current_buckets[other_bucket] += amount
            actions += 1
    buckets = [bucket_one, bucket_two]
    actions = 1
    current_buckets = [0, 0]
    current_buckets[start_bucket - 1] = buckets[start_bucket - 1]
    while True:
        other_bucket = 1 - start_bucket
        if current_buckets[start_bucket - 1] == goal:
            return actions, start_bucket, current_buckets[other_bucket]
        if current_buckets[other_bucket] == goal:
            return actions, other_bucket + 1, current_buckets[start_bucket - 1]
        if current_buckets[start_bucket - 1] == 0:
            current_buckets[start_bucket - 1] = buckets[start_bucket - 1]
            actions += 1
        elif current_buckets[other_bucket] == buckets[other_bucket]:
            current_buckets[other_bucket] = 0
            actions += 1
        else:
            amount = min(current_buckets[start_bucket - 1], buckets[other_bucket] - current_buckets[other_bucket])
            current_buckets[start_bucket - 1] -= amount
            current_buckets[other_bucket] += amount
            actions += 1
