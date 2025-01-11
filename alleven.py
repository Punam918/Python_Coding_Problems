L = []
for i in range(1000,3001):
  flag = True

  curr = i

  while curr > 0:
    last = curr%10
    if last % 2 != 0:
      flag = False
      break
    curr = curr//10

  if flag == True:
    L.append(str(i))

print(",".join(L))