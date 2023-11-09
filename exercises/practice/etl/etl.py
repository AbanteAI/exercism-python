def transform(legacy_data):
    new_format = {}
    for point_value, letters in legacy_data.items():
        for letter in letters:
            new_format[letter.lower()] = point_value
    return new_format