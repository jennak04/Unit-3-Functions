
def calculate_discount(price, member_status):
    if member_status == "premium":
       return price * 0.7
        
    elif member_status == "standard":
        return price * 0.85
    
    else:
        return price
    
print(calculate_discount(100, "premium"))
print(calculate_discount(100, "standard"))
print(calculate_discount(100, "guest"))

def count_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for i in text:
        if i in vowels:
            vowel_count += 1
    return vowel_count

print(count_vowels("\nHello World"))

def validate_password(password):
    if len(password) < 8:
        return False
    
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            
    return has_digit
