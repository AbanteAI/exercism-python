def measure(bucket_one, bucket_two, goal, start_bucket):
    def pour(bucket_a, bucket_b, max_bucket_b):
        remaining = max_bucket_b - bucket_b
        poured = min(bucket_a, remaining)
        return bucket_a - poured, bucket_b + poured

    if start_bucket == "one":
        current_bucket_one, current_bucket_two = bucket_one, 0
    else:
        current_bucket_one, current_bucket_two = 0, bucket_two

    steps = 0
    visited_states = set()

    while (current_bucket_one, current_bucket_two) not in visited_states:
        visited_states.add((current_bucket_one, current_bucket_two))

        if current_bucket_one == goal or current_bucket_two == goal:
            break

        if current_bucket_one == 0:
            current_bucket_one = bucket_one
        elif current_bucket_two == bucket_two:
            current_bucket_two = 0
        else:
            current_bucket_one, current_bucket_two = pour(current_bucket_one, current_bucket_two, bucket_two)

        steps += 1

    if current_bucket_one == goal:
        return steps, "one", current_bucket_two
    else:
        return steps, "two", current_bucket_one