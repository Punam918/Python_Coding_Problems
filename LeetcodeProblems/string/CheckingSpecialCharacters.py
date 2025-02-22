# Program to check if a string contains any special character
'''
Input: Geeks$For$Geeks
Output: String is not accepted.

Input: Geeks For Geeks
Output: String is accepted
'''
import re

def contains_special_character(s):
    pattern = r"[!@#$%^&*()_+{}\[\]:;'<>,.?/~`\\|-]"    
    if re.search(pattern, s):
        return True
    return False

string = "Hello@World!"
if contains_special_character(string):
    print("The string contains special characters.")
else:
    print("No special characters found.")
