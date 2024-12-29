#mississipp to ssssiiippm
from collections import Counter

def wordcountandtransform(s):
    # Count the frequency of each character
    freq = Counter(s)
    
    # Sort characters first by frequency (descending) and then by order of appearance
    sorted_chars = sorted(s, key=lambda x: (-freq[x], s.index(x)))
    
    # Join the sorted characters into a string
    transformed = ''.join(sorted_chars)
    
    return transformed

# Example usage
print(wordcountandtransform('mississipp'))