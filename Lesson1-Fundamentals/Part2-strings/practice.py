def create_username(first_name, last_name):
   # username = first_name + "_" + last_name
    return f"{first_name}_{last_name}".lower()

print(create_username("John", "Smith"))
print(create_username("MARY", "Smith"))

def check_email(email):
    email_lower = email.lower()
    
   # if "@" and email_lower and email_lower.endsWith(".com"):
      #  return True
   # else:
     #   return False
     
     #second way
   # return "@" in email_lower and email_lower.endswith(".com")

def create_slug(title):
    return title.strip().replace(" ", "-").lower()

print(create_slug("My First Blog Post"))
print(create_slug(" Python Tutorial "))
    
    

    

