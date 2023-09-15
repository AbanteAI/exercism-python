def measure(bucket_one, bucket_two, goal, start_bucket):
    actions = 0
    bucket1 = 0
    bucket2 = 0

    if start_bucket == "one":
        bucket1 = bucket_one
    else:
        bucket2 = bucket_two

    while bucket1 != goal and bucket2 != goal:
        if bucket1 == 0:
            bucket1 = bucket_one
            actions += 1
        elif bucket2 == bucket_two:
            bucket2 = 0
            actions += 1
        elif bucket1 > 0 and bucket2 < bucket_two:
            transfer = min(bucket1, bucket_two - bucket2)
            bucket1 -= transfer
            bucket2 += transfer
            actions += 1

    if bucket1 == goal:
        return (actions, "one", bucket2)
    else:
        return (actions, "two", bucket1)
