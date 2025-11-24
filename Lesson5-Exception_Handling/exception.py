def safe_divide(a,b):
    try:
        result  = a / b
        return result
    except ZeroDivisionError: # only its a zero division
        print("Can not divide by 0")
        return None
    except TypeError:
        print("Thats not a valid number")
        return None
    except:
        print("An error occurred")
        
#print(safe_divide(10,2)) #5.0
#print(safe_divide(10,0)) 
#print(safe_divide(10,"hello")) 

def safe_operations(a,b,list,key,d):
    try:
        print(f"Division result: {a/b}") #ZeroDivisonError, TypeError
        print("Access list element:" ,list[2]) #IndexError
        print("Access Dictionary Key:" ,d[key]) #KeyError
        print(f"Add numbers: {a+b}")
        
    except ZeroDivisionError:
        print("Can not divide by zero!")
    except IndexError:
        print("List index out of range!")
    except KeyError:
        print(f"Key {key} not found in dictionary!")
    except TypeError:
        print("Invalid types for operation!")
    except Exception as e: # finding out what the error is
        print("Some other error occured", e)
        
#print(safe_operations(10,2,[1,2], "Tom", {"John": 15}))
#print(safe_operations(10,0,[1,2], "Tom", {"John": 15}))
print(safe_operations(10,"hello",[1,2], "Tom", {"Tom": 15}))

def calculate_price_per_item(total_cost, num_items):
    try:
        return f"${total_cost / num_items:.2f}"
    except ZeroDivisionError:
        return f"No items entered"
    
print(calculate_price_per_item(144, 4))

def parse_age(age):
    try:
        return int(age)
    
    except ValueError:
        return None

print(parse_age("25"))
print(parse_age("2-5"))

    
