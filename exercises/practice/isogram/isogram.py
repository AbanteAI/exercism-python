def is_isogram(string):
    # Remove spaces and hyphens from the string
    string = string.replace(" ", "").replace("-", "").lower()

    # Check if the string has any repeating letters
    return len(string) == len(set(string))
