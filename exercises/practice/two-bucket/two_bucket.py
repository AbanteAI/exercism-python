import math

    if goal % math.gcd(bucket_one, bucket_two) != 0:
        raise ValueError("Goal cannot be reached with given bucket sizes")
    
    if start_bucket == "one":
        current_bucket = [bucket_one, 0]
    else:
        current_bucket = [0, bucket_two]
    
    num_actions = 0
    
    while True:
        if current_bucket[0] == goal or current_bucket[1] == goal:
            break
        
        if current_bucket[0] == 0:
            current_bucket[0] = bucket_one
        elif current_bucket[1] == bucket_two:
            current_bucket[1] = 0
        elif current_bucket[1] < bucket_two:
            transfer_amount = min(current_bucket[0], bucket_two - current_bucket[1])
            current_bucket[0] -= transfer_amount
            current_bucket[1] += transfer_amount
        num_actions += 1
    
    if current_bucket[0] == goal:
        other_bucket = current_bucket[1]
    else:
        other_bucket = current_bucket[0]
    
    return num_actions, "one" if current_bucket[0] == goal else "two", other_bucket

