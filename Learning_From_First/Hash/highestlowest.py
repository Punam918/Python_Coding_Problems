from collections import Counter

def find_highest_and_lowest_frequency(arr):

    freq = Counter(arr)    
    max_freq = max(freq.values())
    min_freq = min(freq.values())

    highest = [key for key, value in freq.items() if value == max_freq]
    lowest = [key for key, value in freq.items() if value == min_freq]

    print("Highest frequency elements:", highest)
    print("Lowest frequency elements:", lowest)


arr = [10, 5, 10, 15, 10, 5]
find_highest_and_lowest_frequency(arr)
