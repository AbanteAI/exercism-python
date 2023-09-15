def measure(bucket_one, bucket_two, goal, start_bucket):
    def pour(bucket_a, bucket_b):
        transfer = min(bucket_a[1], bucket_b[0] - bucket_b[1])
        return (bucket_a[0], bucket_a[1] - transfer), (bucket_b[0], bucket_b[1] + transfer)

    if start_bucket == "one":
    if goal > max(bucket_one, bucket_two):
        raise ValueError("The goal is larger than both buckets.")
        start = [(bucket_one, 0), (bucket_two, 0)]
    else:
        start = [(bucket_two, 0), (bucket_one, 0)]

    visited = set()
    queue = [(0, start)]

    while queue:
        steps, state = queue.pop(0)
        for bucket in state:
            if bucket[1] == goal:
                other_bucket = state[1] if state[0] == bucket else state[0]
                return steps, start_bucket, other_bucket[1]

        state_tuple = tuple(state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        next_states = [
            (steps + 1, (state[0], (state[1][0], 0))),
            (steps + 1, ((state[0][0], 0), state[1])),
            (steps + 1, pour(state[0], state[1])),
            (steps + 1, pour(state[1], state[0])),
            (steps + 1, ((state[0][0], state[0][0]), state[1])),
            (steps + 1, (state[0], (state[1][0], state[1][0]))),
        ]
        queue.extend(next_states)