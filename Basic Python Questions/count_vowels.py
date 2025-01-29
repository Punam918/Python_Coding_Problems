def checkvowels(s):
    vow = 'aeiouAEIOU'
    return sum(1 for char in s if char in vow)
    
value = input("enter what you need to check")
print(checkvowels(value))