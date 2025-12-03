# question 15
def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    return average

grades = []
result = calculate_average(grades)
print(f"Average: {result}")

# the variable "grades" is a empty list, which causes a ZeroDivisionError

# question 16
# C) required → *args → defaults → **kwargs

# question 17
text = " Hello Python World "

# Remove whitespace from both ends
clean = text.strip()

# Convert to uppercase
upper = text.upper()

# Split into a list of words
words = text.strip().split()

# Get the length of the cleaned text
length = len(text.strip())

# question 18
def validate_password(password):
    if not password:
        return False, "Empty Password"
    
    if len(password) < 8:
        return False, "Too short"
    
    return True, "Valid"

print(validate_password(""))
print(validate_password("a"))
print(validate_password("abcdefghijk"))

# question 19
def create_invetory(item_name, *quantities, location="Warehouse"):
    total = sum(quantities) if quantities else 0
    return {
        "item": item_name,
        "total": total,
        "location": location
    }

print(create_invetory("Widget", 10,20,15))

# question 20
def safe_list_access(items, index):
    try:
        return items[index], True
    
    except IndexError:
        return None, False
    
print(safe_list_access([10, 20, 30], 1)) 
print(safe_list_access([10, 20, 30], 10)) 
print(safe_list_access([], 0))
