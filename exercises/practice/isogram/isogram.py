def is_isogram(string):
    # Normalize the string by converting it to lowercase and removing hyphens and spaces
    normalized_string = string.replace("-", "").replace(" ", "").lower()
    
    # Use a set to track unique characters
    seen = set()
    
    # Iterate over each character in the normalized string
    for char in normalized_string:
        # If the character is already in the set, it's not an isogram
        if char in seen:
            return False
        seen.add(char)
    
    # If no characters repeat, it's an isogram
    return True