# question 1
def process_order(customer, *items, discount=0.0, **options):
    total = len(items) * 10 
    total -= total * discount
    if options.get("express"): # check for express 
            total += 5 # add 5 dollars if there is express
    return round(total, 2)

print(process_order("A","book","pen", discount=0.1)) #18.0

print(process_order("B","laptop", express=True)) #15.0

# question 2
def make_notification(user, *messages, urgent=False):
    text = ", ".join(messages)

    if urgent:
        return f"URGENT: {user} - {text}"
    return f"{user} - {text}"

print(make_notification("admin", "Server down!", urgent=True))  # Should return: "URGENT: admin - Server down!"
print(make_notification("user", "Welcome", "Check inbox"))  # Should return: "user - Welcome, Check inbox"

# question 3
def build_query(table, *fields, where="", limit=10):
    field_str = ",\n".join(fields) if fields else "*"

    query = f"SELECT {field_str} FROM {table}"
    if where: # if where has something inside of it
        query += f" WHERE {where}"
    if limit: # if limit has something inside of it
        query += f" LIMIT {limit}"
    return query


print(build_query("users", "name", "email")) # SELECT name,
                                            # email FROM users LIMIT 10
print(build_query("logs", where="level='error'", limit=5)) # SELECT * FROM logs WHERE level='error' LIMIT 5

# question 4
def log_action(actor, *actions, timestamp=None, **context):
    all_actions = ", ".join(actions)
    context_parts = []
    for key, value in context.items():
        context_parts.append(f"{key}={value}")
    context_all = ", ".join(context_parts)
        
    return f"{actor}: {all_actions} | {context_all}"

print(log_action("bot", "login", "scan", source="API", ip="1.2.3.4"))  # Should return: "bot: login, scan | source=API, ip=1.2.3.4"
 