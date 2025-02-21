# Find all close matches of input string from a list
s = ["Lion", "Li", "Tiger", "Tig"]
a = "Lion"
for string in s:
    if string.startswith(a) or a.startswith(string):
        print(string, end=" ")