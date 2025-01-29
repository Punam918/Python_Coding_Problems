# Write code here
N = int(input('enter the number'))
sum = 0
i = 1

while i < N+1:
  if i % 5 == 0:
    i+=1
    continue

  sum += i

  if sum > 300:
    sum = sum - i
    break

  i+=1

print(sum)