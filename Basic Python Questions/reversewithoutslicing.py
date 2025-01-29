# Write code here
number = int(input('enter the number'))

rev = 0

while number>0:
  last = number%10
  rev = rev*10 + last
  number = number//10

print(rev)