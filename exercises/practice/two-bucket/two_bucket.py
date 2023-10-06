def measure(bucket_one, bucket_two, goal, start_bucket):
    def pour(bucket_a, bucket_b):
        poured = min(bucket_a["content"], bucket_b["capacity"] - bucket_b["content"])
        bucket_a["content"] -= poured
        bucket_b["content"] += poured
        return poured

    buckets = {
        "one": {"capacity": bucket_one, "content": 0},
        "two": {"capacity": bucket_two, "content": 0}
    }

    steps = 0
    current_bucket = start_bucket
    other_bucket = "two" if start_bucket == "one" else "one"

    while buckets[current_bucket]["content"] != goal and buckets[other_bucket]["content"] != goal:
        if buckets[current_bucket]["content"] == 0:
            buckets[current_bucket]["content"] = buckets[current_bucket]["capacity"]
        elif buckets[other_bucket]["content"] == buckets[other_bucket]["capacity"]:
            buckets[other_bucket]["content"] = 0
        else:
            pour(buckets[current_bucket], buckets[other_bucket])

        steps += 1

        if (buckets[current_bucket]["content"] == 0 and buckets[other_bucket]["content"] == buckets[other_bucket]["capacity"]) or (buckets[current_bucket]["content"] == buckets[current_bucket]["capacity"] and buckets[other_bucket]["content"] == 0):
            steps -= 1
            break

    if buckets[current_bucket]["content"] == goal:
        return steps, current_bucket, buckets[other_bucket]["content"]
    else:
        return steps, other_bucket, buckets[current_bucket]["content"]