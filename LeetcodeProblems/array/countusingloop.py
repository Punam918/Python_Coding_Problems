def count_items(arr):
    count = 0
    for item in arr:
        count += 1
    return count

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
item_count = count_items(arr)
print("Number of items:", item_count)
