def private_key(p):
    """
    Generates a private key for the Diffie-Hellman key exchange.

    Args:
        p (int): Prime number.

    Returns:
        int: Private key.
    """
    import random

    return random.randint(2, p - 1)


def public_key(p, g, private):
    """
    Calculates the public key for the Diffie-Hellman key exchange.

    Args:
        p (int): Prime number.
        g (int): Generator.
        private (int): Private key.

    Returns:
        int: Public key.
    """
    return pow(g, private, p)


def secret(p, public, private):
    """
    Calculates the secret key for the Diffie-Hellman key exchange.

    Args:
        p (int): Prime number.
        public (int): Public key.
        private (int): Private key.

    Returns:
        int: Secret key.
    """
    return pow(public, private, p)
