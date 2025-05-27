#counting frequency using hashing in an array

arr = [1,2,3,4,3,3,2,2,6,6,6,7,7,8,8]
def countfreq(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    print("Frequencies of elements:")
    for key, value in freq.items():
        print(f"{key}: {value}")
print(countfreq([1,2,3,4,3,3,2,2,6,6,6,7,7,8,8]))

