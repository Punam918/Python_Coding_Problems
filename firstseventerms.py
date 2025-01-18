x = 10
n = 5

sum = 0
s = ''
for i in range(1,n+1):
  sum = sum + (1/i)*((x-1)/x)**i
  s = s + '(1/{})*((x-1)/x)^{} +'.format(i,i)
print(s[:-1])
print(sum)