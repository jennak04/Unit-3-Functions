# question 1
kills = [3, 0, 5, 2, 8, 1, 7]
streaks = []
current = 0

for k in kills:
    if k > 0:
        current += k 
    else:
        if current >= 5:
            streaks.append(current) 
        current = 0 #resets current at first index
if current >= 5:
    streaks.append(current)
print(streaks) #[23]

# question 2
player = "[NEXUS] ShadowViper"
tag = ""
i = 1
while player[i] != "]":
    tag += player[i]
    i += 1
print(tag) # prints NEXUS, everything inside the bracket

# question 3
def match_mvp(players):
    Highest_ratio = 0
    highest_player = ""
    
    for player, values in players.items():
        kd_ratio = values["kills"] / values["deaths"]
        if kd_ratio > Highest_ratio:
            Highest_ratio = kd_ratio
            highest_player = player
    return highest_player 
    
players = {
    "phoenix": {"kills": 28, "deaths": 12},
    "cipher": {"kills": 35, "deaths": 15},
    "blaze": {"kills": 22, "deaths": 18}
}

print(match_mvp(players))