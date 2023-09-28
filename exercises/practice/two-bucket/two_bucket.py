def measure(bucket_one, bucket_two, goal, start_bucket):
    if start_bucket == "one":
        if bucket_one >= goal:
            return (1, "one", goal)
        elif bucket_one + bucket_two < goal:
            return (bucket_one + bucket_two, "two", 0)
        else:
            # Measure using bucket_one and bucket_two
            actions = 1
            current_bucket_one = bucket_one
            current_bucket_two = 0
            while current_bucket_one != goal and current_bucket_two != goal:
                if current_bucket_one == 0:
                    current_bucket_one = bucket_one
                    actions += 1
                elif current_bucket_two == bucket_two:
                    current_bucket_two = 0
                    actions += 1
                else:
                    transfer_amount = min(current_bucket_one, bucket_two - current_bucket_two)
                    current_bucket_one -= transfer_amount
                    current_bucket_two += transfer_amount
                    actions += 1

            if current_bucket_one == goal:
                return (actions, "one", current_bucket_two)
            else:
                return (actions, "two", current_bucket_one)
    elif start_bucket == "two":
        if bucket_two >= goal:
            return (1, "two", goal)
        elif bucket_one + bucket_two < goal:
            return (bucket_one + bucket_two, "one", 0)
        else:
            # Measure using bucket_two and bucket_one
            actions = 1
            current_bucket_two = bucket_two
            current_bucket_one = 0
            while current_bucket_one != goal and current_bucket_two != goal:
                if current_bucket_two == 0:
                    current_bucket_two = bucket_two
                    actions += 1
                elif current_bucket_one == bucket_one:
                    current_bucket_one = 0
                    actions += 1
                else:
                    transfer_amount = min(current_bucket_two, bucket_one - current_bucket_one)
                    current_bucket_two -= transfer_amount
                    current_bucket_one += transfer_amount
                    actions += 1

            if current_bucket_two == goal:
                return (actions, "two", current_bucket_one)
            else:
                return (actions, "one", current_bucket_two)
    else:
        raise ValueError("Invalid start_bucket value. Must be either 'one' or 'two'.")
