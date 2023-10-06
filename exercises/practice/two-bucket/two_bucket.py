import math
def measure(bucket_one, bucket_two, goal, start_bucket):
    if goal % math.gcd(bucket_one, bucket_two) != 0:
        raise ValueError("No solution")
    if start_bucket == "one":
        small_bucket, large_bucket = min(bucket_one, bucket_two), max(bucket_one, bucket_two)
    else:
        small_bucket, large_bucket = max(bucket_one, bucket_two), min(bucket_one, bucket_two)
    actions = 1
    while small_bucket != goal and large_bucket != goal:
        if small_bucket == 0:
            small_bucket = bucket_one
            actions += 1
        elif large_bucket == large_bucket:
            large_bucket = 0
            actions += 1
        else:
            transfer = min(small_bucket, large_bucket - large_bucket)
            small_bucket -= transfer
            large_bucket += transfer
            actions += 1
    return actions, "one" if small_bucket == goal else "two", large_bucket