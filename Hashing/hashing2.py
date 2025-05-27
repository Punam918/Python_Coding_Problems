def maxfreqelements(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1  

    maxfreq = max(freq.values())
    highest_freq_elements = [k for k, v in freq.items() if v == maxfreq]
    
    print("Highest element(s) with highest frequency:", highest_freq_elements)
maxfreqelements([2, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 3, 4, 4, 4, 44, 4])
