
# 2+22+222+2222+22222
# Sum of above series is: 24690

x = 10
n = 5

sum = 1
s = ''
print('1 + ',end='')
for i in range(2,n+1):
  sum = sum + x**i/i
  s = s + 'x^{}/{} +'.format(i,i)
print(s[:-1])
print(sum)