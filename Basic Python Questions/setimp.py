def duplicate_encode(word):
    normalized = word.lower()
    char_count = {}
    
    for char in normalized:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char] = 1
        
    result = ""
    for char in normalized:
        if char_count[char] == 1:
            result+="("
        else:
            result+=")"
    return result


