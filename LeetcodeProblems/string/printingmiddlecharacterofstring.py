# Input: str = “Java”
# Output: v
# Explanation: 
# The length of the given string is even. 
# Therefore, there would be two middle characters ‘a’ and ‘v’, we print the second middle character.


# Input: str = “GeeksForGeeks”
# Output: o
# Explanation: 
# The length of the given string is odd. 
# Therefore, there would be only one middle character, we print that middle character.

def findmiddlecharacter(str):
    leng = len(str)
    middle = leng//2
    return str[middle]
print(findmiddlecharacter('Java'))
print(findmiddlecharacter('GeeksForGeeks'))

