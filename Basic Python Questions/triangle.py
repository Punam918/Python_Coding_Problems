first = int(input('enter the 1st angle'))
second = int(input('enter the 2nd angle'))
third = int(input('enter the 3rd angle'))

if (first+second+third) == 180 and first>0 and second>0 and third>0:
  print('forms a triangle')
else:
  print('does not form a triangle')