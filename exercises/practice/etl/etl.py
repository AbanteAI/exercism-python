def transform(legacy_data):
    points = {}
    for key, values in legacy_data.items():
        letter = key.lower()
        for score in values:
            points[letter] = score
    return points