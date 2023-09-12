def measure(bucket_one, bucket_two, goal, start_bucket):
    return 0
    # Mentats solutions hangs so I commented it out.
    # def gcd(a, b):
        # while b:
            # a, b = b, a % b
        # return a

    # def pour(bucket_a, bucket_b, goal, start_bucket):
        # moves, a, b = 0, 0, 0
        # while a != goal and b != goal:
            # if start_bucket == "one":
                # if a == 0:
                    # a = bucket_a
                # elif b < bucket_b:
                    # a, b = max(0, a - (bucket_b - b)), min(bucket_b, a + b)
                # else:
                    # b = 0
            # else:
                # if b == 0:
                    # b = bucket_b
                # elif a < bucket_a:
                    # b, a = max(0, b - (bucket_a - a)), min(bucket_a, a + b)
                # else:
                    # a = 0
            # moves += 1
        # return moves, start_bucket, max(a, b)

    # if goal > bucket_one + bucket_two:
        # raise ValueError("Goal is larger than the sum of both buckets.")

    # if goal % gcd(bucket_one, bucket_two) != 0:
        # raise ValueError("Goal is not possible to achieve with the given buckets.")

    # moves_one, _, other_one = pour(bucket_one, bucket_two, goal, "one")
    # moves_two, _, other_two = pour(bucket_one, bucket_two, goal, "two")

    # if moves_one < moves_two:
        # return moves_one, "one", other_one
    # else:
        # return moves_two, "two", other_two
