def format_phone_number(phone):
    digits = phone.replace("-", "").replace(" ", "").replace("(", "").replace(")", "")
    
    if len(digits) != 10 or not digits.isdigit():
        return "Invalid Phone Number"
    
    chunk1 = digits[0:3]
    chunk2 = digits[3:6]
    chunk3 = digits[6:]
    
    return f"({chunk1}) {chunk2}-{chunk3}"

print(format_phone_number("555-123-1245"))
print(format_phone_number("1"))