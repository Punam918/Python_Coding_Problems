start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for num in range(start, end+1):
    temp = num
    sum = 0
    order = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num)