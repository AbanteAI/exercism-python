def convert(number):
    factors = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    result = [sound for factor, sound in factors.items() if number % factor == 0]
    return ''.join(result) or str(number)