# question 1

def get_phone_number(contacts, name):
    try:
            return contacts[name]
    
    except KeyError: 
        return "Contact not found"
    
# contact exists
contacts = {"Mom": "555-0123", "Dad": "555-0124", "Best Friend": "555-0125"}
print(get_phone_number(contacts, "Mom"))

# contact doesn't exist
contacts = {"Mom": "555-0123", "Dad": "555-0124", "Best Friend": "555-0125"}
print(get_phone_number(contacts, "Boss"))

# question 2
def get_song(list_songs, position):
    try:
        return list_songs[position]
    
    except IndexError: 
        return "Position out of range"
    
    except TypeError:
        return "Position must be an integer"
    
# valid position
playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"]
print(get_song(playlist, 2))

# position out of range
playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"]
print(get_song(playlist, 20))

# invalid position type
playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"]
print(get_song(playlist, "first"))

# question 3
def calculate_test_average(list_scores):
    
    try: 
        total = sum(list_scores)
        length = len(list_scores)
    
        average = total / length
        return round(average, 2)
    
    except ZeroDivisionError:
        return 0
    
    except TypeError:
        return "Invalid Score Data"
    
# valid test scores
print(calculate_test_average([88,92,76,95,84]))
    
# decimal test scores
print(calculate_test_average([78.5, 92.0, 85.5]))

# empty list
print(calculate_test_average([]))


    
    
        



        
    
        