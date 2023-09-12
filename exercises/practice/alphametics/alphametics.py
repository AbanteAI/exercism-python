from itertools import permutations

def solve(puzzle):
    words = [word for word in puzzle.split(' ') if word.isalpha()]
    unique_chars = sorted(list(set(''.join(words))))
    if len(unique_chars) > 10:
        return None

    def valid_solution(mapping):
        trans = str.maketrans(''.join(unique_chars), ''.join(mapping))
        translated_words = [word.translate(trans) for word in words]
        numbers = [int(word) for word in translated_words]
        if any(str(number)[0] == '0' for number in numbers):
            return False
        return sum(numbers[:-1]) == numbers[-1]

    for mapping in permutations('0123456789', len(unique_chars)):
        if valid_solution(mapping):
            return dict(zip(unique_chars, [int(c) for c in mapping]))

    return None