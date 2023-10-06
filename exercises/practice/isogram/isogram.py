def is_isogram(string):
    # Remove spaces and hyphens from the string
    string = string.replace(" ", "").replace("-", "")
    
    # Convert string to lowercase for case-insensitive comparison
    string = string.lower()
    
    # Create a set to store unique characters
    unique_chars = set()
    
    # Iterate through each character in the string
    for char in string:
        # If the character is already in the set, it is not an isogram
        if char in unique_chars:
            return False
        # Add the character to the set
        unique_chars.add(char)
    
    # If no repeating characters were found, it is an isogram
    return True

