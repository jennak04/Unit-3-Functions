# question 1
viewers = [1240, 1580, 2100, 1890, 2300]
peak = viewers[0] #1240
i = 1

while i < len(viewers):
    if viewers[i] > peak:
        peak = viewers[i] #1580, then 2100, then 2300
    i += 1

print(peak) # 2300

# question 2
message = "WOW POGGERS WOW LFG"
words = message.split() # ["WOW", "POGGERS", "WOW", "LFG"]
filtered = ""

for word in words:
    if len(word) <= 5:
        filtered += word + " "
print(filtered.strip()) # "WOW WOW LFG"

# question 3
def find_top_donor(donation):
    top_donation = 0
    top_donator = ""
    
    for donator, donation in donation.items():
        if donation > top_donation:
            top_donation = donation
            top_donator = donator
    return top_donator
            
    
donations = {
    "neon": 250,
    "vibe": 180,
    "lunar": 400,
    "pixel": 150
}

print(find_top_donor(donations))