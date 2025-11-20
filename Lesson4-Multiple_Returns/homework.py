# question 1
def search_user_database(user):
    if user == "" or " ":
        return None, "No search query", False
    
    if not user.isalpha():
        return False, "Invalid Characters", False
    
result, message, success = search_user_database("")
print(result) # None
print(message) # "No search query"
print(success) # False
    

# question 2
def analyze_book_pages(books):
    total = len(books)
    total_pages = sum(books)
    average_pages = sum(books) / len(books)
    has_long = False
    for pages in books:
        if pages > 500:
            has_long = True
    return total, total_pages, average_pages, has_long

count, total, avg, has_long = analyze_book_pages([250, 180, 620, 310])
print(count) # 4
print(total) # 1360
print(avg) # 340.0
print(has_long) # True (because 620 > 500)
