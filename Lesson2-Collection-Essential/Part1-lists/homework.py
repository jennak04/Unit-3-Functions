# Problem 1:
def remove_duplicates(items):
    removed_dupes = []
    for i in items:
        if i not in removed_dupes:
            removed_dupes.append(i)
    return removed_dupes
    
print("REMOVE DUPLICATES")
print(remove_duplicates(["a", "b", "a", "c"]))
print(remove_duplicates([5, 5, 5]))
print(remove_duplicates([]))
print(remove_duplicates([1, 2, 2, 3, 1, 4]))
print(remove_duplicates(["a", "b", "a", "c"]))
print(remove_duplicates([5, 5, 5]))
print(remove_duplicates([]))

# Problem 2:
def find_common(list1, list2):
    commons = []
    for i1 in list1:
        for i2 in list2:
            if i1 == i2:
                commons.append(i1)
                
    return commons

print("\nFIND COMMONS")
print(find_common([1, 2, 3], [2, 3 ,4]))
print(find_common(["a", "b"], ["c", "d"]))
print(find_common([1, 1, 2], [2, 2, 3]))
print(find_common([], [1, 2]))

# Problem 3:
print("\nREVERSE")
def reverse_sublists(data, size):
    reverse = []
    for i in range(0, len(data), size):
        chunk = data[i:i+size] #chunk = [1,2]
        for i in range(len(chunk)-1, -1, -1): #i=1, i=0
            reverse.append(chunk[i]) # reverse = [2,1]
    return reverse

print(reverse_sublists([1, 2, 3, 4, 5, 6], 2))
print(reverse_sublists([1, 2, 3, 4, 5], 3))
print(reverse_sublists([1, 2, 3, 4], 1))
print(reverse_sublists([1, 2, 3], 5))


# Problem 4:
print("\nROTATE LIST")
def rotate_lists(item, position):
    rotate = position % len(item)
    result = []
    
    for i in range(len(item)):
        new_pos = (i - rotate) % len(item)
        result.append(item[new_pos])
        
    return result

print(rotate_lists([1, 2, 3, 4, 5], 2))
print(rotate_lists([1, 2, 3, 4, 5], -2))
print(rotate_lists([1, 2, 3], 0))
print(rotate_lists([1, 2, 3], 5))