def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

s = "hello"
reversed_s = reverse_string(s)
print("Reversed String:", reversed_s)
