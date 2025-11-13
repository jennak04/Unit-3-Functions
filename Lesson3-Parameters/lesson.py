# using keyword arguments
def create_gamer_profile(username, level, xp, rank, online):
    """Create a gamer profile."""
    return {
        "username": username,
        "level": level,
        "xp": xp,
        "rank": rank,
        "online": online
    }
    
player1 = create_gamer_profile(username="BTstudent", 
                               level=25,
                               rank="Gold",
                               xp=10000,
                               online=True)

print(player1)

def send_message(sender, recipient, message, urgent):
    return f"{sender} -> {recipient}: {message} (Urgent: {urgent})"

message = send_message(sender="Jack",
                       recipient="James",
                       message="Hi",
                       urgent=False)

print(message)

def post_content(username, text, likes=0, retweets=0):
    return f"@{username}: {text} | ❤️ {likes} 🔁 {retweets}"

post = post_content("jenna", "hi")

print(post)

# *args - accept any number of values

def sum_scores(*scores):
    """Sum ANY number of scores"""
    total = 0
    for score in scores:
        total += score
    return total

result = sum_scores(10, 20, 30)
result2 = sum_scores(10,20,30,40,55,60)


