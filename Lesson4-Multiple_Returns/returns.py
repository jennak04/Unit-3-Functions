def search_data(query):
    if query == "": # no query provided
        return None
    if query == "empty": #found zero results
        return 0
    if query == "error":
        return False # search failed
    return len(query) # normal case - return count

# return type - None -> No value
# Meaning: absecne of value, not set, not found
# use for: missing data, search failures, optional parameters

result = None
print(result is None) # True - identity check
print(result == None) # True - equality check
print(not result) # True - falsy check

#2 Return Type - false
# meaning: explicit false condition, validation failure, negative result

#use for: validation result, boolean operations, success/failure status

result = False
print(result is False) # True - identity check
print(not result) # True - boolean negation
print(result == 0) # True - falsy check

#3 Return zero - a valid number
# 0 is VALID numeric value, not absence of value!

result = 0
print(result == 0) # True - numeric equality
print(not result) # True - (falsy in boolean context)
print(result is None) # False - different objects
print(result is False) # False - different types