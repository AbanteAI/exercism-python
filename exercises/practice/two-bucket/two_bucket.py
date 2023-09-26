def measure(bucket_one, bucket_two, goal, start_bucket):
    buckets = [bucket_one, bucket_two]
    actions = 1
    current_bucket = int(start_bucket == "two")
    other_bucket = 1 - current_bucket

    while buckets[current_bucket] != goal and buckets[other_bucket] != goal:
        if buckets[current_bucket] == 0:
            buckets[current_bucket] = bucket_one if current_bucket == 1 else bucket_two
            actions += 1
        elif buckets[other_bucket] == buckets[other_bucket]:
            buckets[other_bucket] = 0
            actions += 1
        else:
            transfer = min(buckets[current_bucket], bucket_two - buckets[other_bucket])
            buckets[current_bucket] -= transfer
            buckets[other_bucket] += transfer
            actions += 1

    return (actions, current_bucket, buckets[other_bucket])
