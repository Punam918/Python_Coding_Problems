n = int(input('enter the number'))  # enter a number
binary = [] # create an empty list
while n > 0: # loop until n is greater than 0

  binary.append(n%2)     # append the remainder of n divided by 2 to the list 13%2 = 1, 6%2 = 0, 3%2 = 1, 1%2 = 1
  n = n//2               # divide n by 2 and assign the result to n 13//2 = 6, 6//2 = 3, 3//2 = 1, 1//2 = 0

for i in binary[::-1]: # loop through the list in reverse
  print(i,end='')   # print the elements of the list