num = int(input('enter the num'))

flag = True
for i in range(2,num):
  if num%i == 0:
    flag = False
    break

if flag == True:
  print('Prime')
else:
  print('Not Prime')
