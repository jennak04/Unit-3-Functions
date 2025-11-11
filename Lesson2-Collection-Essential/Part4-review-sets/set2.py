# question 1

prices = [58200, 59500, 61000, 59800, 62500, 64000]
gains = []
i = 1

while i < len(prices):
    diff = prices[i] - prices[i-1] # takes price and the price before it
    if diff > 1000:
        gains.append(diff) # [1300, 1500, 2700, 1500]
    i += 1

print(len(gains)) # 4
print(sum(gains)) # 7000

# question 2
wallet = "0x9F1aB3c...dE8f"
short = ""
i = 0
while i < 10:
    short += wallet[i] #0x9F1aB3c.
    i += 1
short += "..." # 0x9F1aB3c....
print(short) # 0x9F1aB3c....

# question 3
def portfolio_value(holdings, prices):
    total = 0
    for coin, amount in holdings.items():
        total += amount * prices[coin]
    return f"{total:.2f}"

holdings = {"BTC": 0.5, "ETH": 8.2, "SOL": 50}
prices = {"BTC": 62400, "ETH": 2480, "SOL": 142}

print(portfolio_value(holdings, prices))