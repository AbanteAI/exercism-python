def rows(letter):
    if letter == 'A':
        return ['A']
    
    diamond = []
    letters = [chr(val) for val in range(ord('A'), ord(letter) + 1)]
    spaces = len(letters) - 1
    
    for i, letter in enumerate(letters):
        row = ' ' * spaces + letter + ' ' * spaces
        diamond.append(row)
        
        if i != len(letters) - 1:
            spaces -= 1
    
    diamond += diamond[:-1][::-1]
    
    return diamond
    
    return diamond
