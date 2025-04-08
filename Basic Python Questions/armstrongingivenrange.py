fro = int(input("Enter from where: "))
to = int(input("Enter up to when: "))
for num in range(fro,to+1):
    temp = num
    sum = 0
    n = len(str(num))
    while temp>0:
        last = temp%10
        sum+=last**n
        temp = temp//10

    if num == sum:
        print(num)