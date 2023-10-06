def can_chain(dominoes):
    if not dominoes:
        return True
    return _can_chain(dominoes, dominoes[0][0], dominoes[0][1])

def _can_chain(dominoes, left, right):
    if not dominoes:
        return left == right
    for i, (l, r) in enumerate(dominoes):
        if l == right:
            if _can_chain(dominoes[:i] + dominoes[i+1:], left, r):
                return True
        elif r == right:
            if _can_chain(dominoes[:i] + dominoes[i+1:], left, l):
                return True
    return False
