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

# Multiple returns - python packs multiple returns into a tuple
def calculate_room(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter #turns into a tuple (area, perimeter)

result = calculate_room(10,5)
print(result)
print(type(result))

print(type((42))) #int
print(type((42,))) #tuple
no_paraenthesis = 1,2,3
print(type(no_paraenthesis))

# unpacking 
area_result, preimeter_result = calculate_room(10, 6)
print(f"Area {area_result}")
print(f"Perimeter {preimeter_result}")

#def student_grade_analyze(*grades):
#    lowest_grade = 100
#    highest_grade = 0
#    average = sum(grades) / len(grades)
        
#    for grade in grades:
#       pass_fail = "Pass" if average > 60 else "Fail"
#        if grade < lowest_grade:
#            lowest_grade = grade
#        if grade > highest_grade:
#            highest_grade = grade
            
#    return pass_fail, lowest_grade, highest_grade, average

#print(student_grade_analyze(1,2,3,4))
#result = student_grade_analyze(90,92,93,94)
#print(type(result))
#print(result)

# correct way
def analyze_grades(*grades):
    if not grades:
        return 0, 0, 0, False
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    passed = average >= 60
    return average, highest, lowest, passed

print(analyze_grades(91,92,93,94))


