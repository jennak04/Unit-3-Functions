# question 1
email = "John.Smith@Gmail.COM"
normalized = email.lower() # converts all letters to lowercase
username = normalized.split("@")[0] # splits the email into two words ["john.smith", "gmail.com"], accesses "john.smith"
domain = normalized.split("@")[1] # accesses "gmail.com"
print(username, domain) # prints "john.smith gmail.com" 

# question 2 
text = "The Quick Brown Fox"
words = text.split() # defaults as space, ["The", "Quick", "Brown", "Fox"]
initials = ""
for word in words:
    initials += word[0].lower() #acceses the first letter of every word and converts it to lowercase
print(initials) # prints "tqbf"

# question 3 - extract domain

def extract_domain(email):
    at_count = 0
    
    for char in email:
        if char == "@":
            at_count += 1
            
    if at_count == 1:
        return email.split("@")[1].lower()
    
    else:
        return "Invalid Email"

print(extract_domain("john@gmail.com"))
print(extract_domain("JANE@YAHOO.COM"))
print(extract_domain("missing.at.sign.com"))
print(extract_domain("too@@many@signs.com"))

# question 4
message = "Hello123World456"
digits = ""
for char in message:
    if char.isdigit(): # checks if the chatacter is a number
        digits += char # if there is a digit in the message, it will be added to the digits string
print(digits)
# will print 123456

#question 5
filename = "my-document.txt"
name_only = filename.replace(".txt", "") # removes ".txt" from the filename string, "my-document"
safe_name = name_only.replace("-", "_") # replaces the "=" with a "_", "my_document"
result = safe_name.upper() #converts "my_document to all uppercase letters", "MY_DOCUMENT"
print(result)
#will print "MY_DOCUMENT"

#question 6
data = "apple,banana,cherry,date"
items = data.split(",") # ["apple", "banana", "cherry", "date"]
longest = items[0] #gets the first item, "apple"
for item in items: # iterates through all the items
    if len(item) > len(longest):
        longest = item # if the length of the item is larger than "apple" which is 5 letters, it gets reassigned as the longest item
print(longest)
# will print banana

#question 7 - filter numbers
def filter_numbers(text):
    result = ""
    for char in text:
        if not char.isdigit():
            result += char
    return result
    
print(filter_numbers("Hello123World456"))
print(filter_numbers("Test 1 2 3"))
print(filter_numbers("Price: $29.99"))
print(filter_numbers("No numbers here!"))


#Question 8
url = "https://example.com/users/profile"
parts = url.split("/") # ["https:", "", "example.com", "users", "profile"]
protocol = parts[0] # "https:"
domain = parts[2] # "example.com"
path = "/".join(parts[3:]) # joins users and profile together, "users/profile"
print(f"{protocol}//{domain}/{path}") # will print "https://example.com/users/profile"

#Question 9 - count characters types
def count_character_types(text):
    letter_count = 0
    digit_count = 0
    space_count = 0
    
    for char in text:
        if "A" <= char <= "Z" or "a" <= char <= "z":
            letter_count += 1
            
        elif char.isdigit():
            digit_count += 1
            
        elif char == " ":
            space_count += 1
            
    return f"letters: {letter_count}, digits: {digit_count}, spaces: {space_count}"

print(count_character_types("Hello 123"))
print(count_character_types("Test2024!"))


