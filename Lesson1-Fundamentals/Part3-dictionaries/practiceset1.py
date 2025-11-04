# question 1
data = {"key_a": "value1", "key_b": 100, "key_c": False}
data["key_d"] = 50 # adds a new key with a value of 50
data["key_b"] = 150 # reassigns "key_b" as 150
x = data.pop("key_c")

print(data) # prints {'key_a': 'value1', 'key_b': 150, 'key_d': 50}
print(x) # prints "False"

# question 2
data = {"val_x": 100, "val_y": 20} 
total = 0

for key, value in data.items():
    total += value

data["val_z"] = total / 2

print(total) # prints 120, because the for loop adds 100 and 20
print(data["val_z"]) # prints 60 because "val_z" is defined as the total / 2

# question 3

def get_user_bio(user):
    bio = user.get("bio")
    if bio == None:
        return "No bio avaiable"
    return bio
    
print(get_user_bio({"username": "coder", "bio": "Python enthusiast"})) # "Python enthusiast"

print(get_user_bio({"username": "newbie"})) # "No bio available"

# question 4
users = [
{"id": 1, "score": 100}, 
{"id": 2, "score": 50},
{"id": 3,"score": 150}]

for user in users:
    user["score"] += 10

print(users[1]["score"]) # prints 60, because it gives the second index score + 10 
print(users[2]["score"]) # prints 160

# question 5
records = [
{"id": "A", "status": True},
{"id": "B", "status": True}, 
{"id": "C"}]

count = 0
for item in records:
    if item.get("status", False):
        count += 1

print(count) # 2

# question 6

def get_total_engagement(post):
    engagement =  post.get("likes", 0) + post.get("comments", 0) + post.get("shares", 0)
    
    return engagement

print(get_total_engagement({"likes": 100, "comments": 20, "shares": 10})) # 130
print(get_total_engagement({"likes": 50, "comments": 5})) # 55
print(get_total_engagement({"views": 1000}))

# question 7
counter = {}
items = ["alpha", "beta", "alpha", "gamma", "alpha"]

for element in items:
    if element in counter:
        counter[element] += 1
    else:
        counter[element] = 1

print(counter["alpha"]) # prints 3, since alpha is in counter three times
print(len(counter)) # prints 3

# question 8
dict_a = {"key1": "value1","key2": 100}

dict_b = dict_a
dict_c = dict_a.copy()

dict_a["key2"] = 200#  {"key1": "value1","key2": 200}
dict_b["key3"] = 50 # {"key1": "value1","key2": 200, "key3": 50}
dict_c["key4"] = True # {"key1": "value1","key2": 100, "key4": True}

print(dict_a) # {"key1": "value1","key2": 200, "key3": 50}
print(dict_c) ## {"key1": "value1","key2": 100, "key4": True}


#question 9
def find_most_followed(users):
    most_followed = ""
    most_followers = 0
    
    for user in users:
        if user["followers"] > most_followers:
            most_followers = user["followers"]
            most_followed = user["username"]
            
    return most_followed if users else None
    
            
users = [
{"username": "alex","followers": 1000},
{"username": "sam","followers": 5000},
{"username": "jordan","followers": 3000}]

print(find_most_followed(users))
