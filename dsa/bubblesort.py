# bubble sort
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_array)
for i in range(n):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
print("Sorted array:", my_array)

'''
It works on adjacent swaps. First look at 64 then look 34 and then sort it 
then again 64 and 25 and swapsagain 64 and 12 and like this.
Then repeat same thing from first until properly sorted. 
https://www.youtube.com/watch?v=M6Vg8SmGMA8&list=PLhR2IpV1b2FwWwviBHRrR118YAaSlyhTU&index=20


TC = o(n**2) two loops one for selecting element one by one 
and other for comparing that element with other one by one.

SC =o(1)
 
'''