def countnumber(n):
    coun = 0
    while n > 0:
        coun+=1
        n = n//10
    return coun

print(countnumber(334455660))