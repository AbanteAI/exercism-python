def measure(bucket_one, bucket_two, goal, start_bucket):
    def pour(bucket_a, bucket_b):
        poured = min(bucket_a[1], bucket_b[0] - bucket_b[1])
        return (bucket_a[0], bucket_a[1] - poured), (bucket_b[0], bucket_b[1] + poured)

    if start_bucket == "one":
        current = (bucket_one, 0), (bucket_two, 0)
    else:
        current = (bucket_two, 0), (bucket_one, 0)

    count = 0
    visited = set()

    while current not in visited:
        visited.add(current)
        count += 1

        if goal in current[0] or goal in current[1]:
            return count, start_bucket, current[1][1] if start_bucket == "one" else current[0][1]

        if current[0][1] == 0:
            current = (current[0][0], current[0][0]), current[1]
        elif current[1][1] == current[1][0]:
            current = current[0], (current[1][0], 0)
        else:
            current = pour(current[0], current[1]), pour(current[1], current[0])[::-1]

    raise ValueError("Not possible to reach the goal.")