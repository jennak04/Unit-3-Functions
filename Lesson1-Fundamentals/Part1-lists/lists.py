'''
create: [1, 2, 3]
add: .append(val)
remove end: .pop()
insert: .insert(index, val)
length: .length len(list)
slice: .slice(start:end)
index: [0]
'''

# creating lists
daily_ikes = [500, 600, 750, 400]
usernames = ["@nasa", "@tswift", "@netflix"]
mixed_data = [500, "likes", "@user123", True]

#accessing elements
first_day = daily_ikes[0]
last_day = daily_ikes[-1]
third_day = daily_ikes[2]

#slicing
first_three = daily_ikes[0:3] #(500, 600, 750)
last_two = daily_ikes[-2:]

#code along - post analyzer
def analyze_post(likes_list):
    if likes_list:
        total = sum(likes_list)
        average = total / len(likes_list)
        best_day = max(likes_list)
        return (average, best_day)
    return "The list is empty"

def format_usernames(handles):
    formatted = []
    for username in handles:
        formatted.append("@" + username)
    return formatted

# test
result = format_usernames(("nasa", "twsift", "netflix"))
print(result)

def filter_trending_posts(likes_list):
    formatted = []
    for likes in likes_list:
        if likes > 1000:
            formatted.append(likes)
    return formatted
    
print(filter_trending_posts([500, 1200, 800, 1500, 600]))
        

