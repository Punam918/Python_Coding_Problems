from collections import Counter

def rearrange_string(s):
    freq = Counter(s)
    sorted_chars = sorted(freq.keys(), key=lambda x: (-freq[x], x))  # Sort by frequency, then alphabetically
    return "".join(char * freq[char] for char in sorted_chars)

s = "mississipp"
result = rearrange_string(s)
print(result)  # Output: "ssssiiippm"



