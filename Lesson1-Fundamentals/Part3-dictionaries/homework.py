# Question 2
def find_top_players(players, min_score):
    """ Return a list of usernames for players with score >= min_score """
    # YOUR CODE HERE
    min_score_players = []
    for player in players:
        if player["score"] >= min_score:
            min_score_players.append(player["username"])
    return min_score_players
# Test it
players = [
    {"username": "DragonSlayer", "score": 8500},
    {"username": "NinjaWarrior", "score": 6200},
    {"username": "MageKing", "score": 9100},
    {"username": "ShadowAssassin", "score": 5800}
]

result = find_top_players(players, 7000)
print(result)  # Should print: ['DragonSlayer', 'MageKing']

# Question 3
playlists = {
    "Workout Mix": ["Eye of the Tiger", "Stronger", "Lose Yourself"],
    "Study Vibes": ["Lofi Beat 1", "Chill Piano", "Rain Sounds"],
    "Party Hits": ["Uptown Funk", "Levitating", "Blinding Lights"]
}

all_songs = []

for playlist_name, songs in playlists.items():
    for song in songs:
        all_songs.append(song.upper())
        
print(f"Total songs: {len(all_songs)}") # will print 9 because there are 9 values
print(f"First song: {all_songs[0]}") # prints first value, which is "EYE OF THE TIGER"
print(f"Last song: {all_songs[-1]}") # prints last value, which is "BLINDING LIGHTS"

# Question 4
def calculate_cart_total(cart):
    total = 0
    for item in cart:
        item_cost = item["price"] * item["quantity"]
        total += item_cost
    return total
    
    
cart = [
    {"item": "Laptop", "price": 899.99, "quantity": 1},
    {"item": "Mouse", "price": 24.99, "quantity": 2},
    {"item": "Keyboard", "price": 79.99, "quantity": 1},
    {"item": "USB Cable", "price": 9.99, "quantity": 3},
]

total = calculate_cart_total(cart)
print(f"Total: ${total:.2f}")