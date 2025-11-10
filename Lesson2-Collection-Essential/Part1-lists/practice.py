def filter_evens(nums):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens

print(filter_evens([1, 2, 3, 4, 5, 6]))

def list_stats(numbers):
    if numbers:
        total = sum(numbers)
        average = total / len(numbers)
        minimum = min(numbers)
        maximum = max(numbers)
    
        return {
        "minimum": minimum,  
        "maximum": maximum,    
        "average": average    
            }

print(list_stats([1, 2, 3, 4]))
    
    