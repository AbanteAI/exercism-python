from collections import deque

def measure(bucket_one, bucket_two, goal, start_bucket):
    if goal > bucket_one and goal > bucket_two:
        raise ValueError("Goal amount cannot be larger than both bucket sizes.")
    
    initial_state = (0, 0, 0)
    visited = {initial_state}
    queue = deque([initial_state])

    while queue:
        b1, b2, actions = queue.popleft()

        if b1 == goal or b2 == goal:
            return actions, "one" if b1 == goal else "two", b1 if b2 == goal else b2

        next_states = [
            (bucket_one, b2, actions + 1),
            (b1, bucket_two, actions + 1),
            (0, b2, actions + 1),
            (b1, 0, actions + 1),
            (b1 - min(b1, bucket_two - b2), b2 + min(b1, bucket_two - b2), actions + 1),
            (b1 + min(b2, bucket_one - b1), b2 - min(b2, bucket_one - b1), actions + 1),
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    raise ValueError("The goal amount cannot be achieved with the given bucket sizes.")