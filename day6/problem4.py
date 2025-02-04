'''
Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
	Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
	Expected Output : ['Green', 'White', 'Black']
'''

listt = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del listt[5]
del listt[4]
del listt[0]
print(listt)