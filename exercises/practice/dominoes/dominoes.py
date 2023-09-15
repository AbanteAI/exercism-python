def can_chain(dominoes):
    if len(dominoes) < 2 or dominoes[0][0] != dominoes[-1][1]:
        return False
        return False
    
    chain = [dominoes[0]]
    
    for i in range(1, len(dominoes)):
        last_number = chain[-1][1]
        next_number = dominoes[i][0]
        
        if last_number != next_number:
            return False
        
        chain.append(dominoes[i])
    
    return True