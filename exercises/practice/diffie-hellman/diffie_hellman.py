def private_key(p):
    import random
    return random.randint(2, p - 1)

def public_key(p, g, private):
    return pow(g, private, p)  # Calculate public key using modular exponentiation


def secret(p, public, private):
    return pow(public, private, p)  # Calculate shared secret key using modular exponentiation
