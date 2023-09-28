def can_chain(dominoes):
    if not dominoes:
        return False
    
    first_domino = dominoes[0]
    last_domino = dominoes[-1]
    
    if first_domino[0] != last_domino[1]:
        return False
    
    chain = [first_domino]
    used_dominoes = {first_domino}
    
    while len(chain) < len(dominoes):
        for domino in dominoes:
            if domino[0] == chain[-1][1] and domino not in used_dominoes:
                chain.append(domino)
                used_dominoes.add(domino)
                break
            elif domino[1] == chain[0][0] and domino not in used_dominoes:
                chain.insert(0, domino)
                used_dominoes.add(domino)
                break
        else:
            return False
    
    return chain[-1][1] == last_domino[0]
    return True
