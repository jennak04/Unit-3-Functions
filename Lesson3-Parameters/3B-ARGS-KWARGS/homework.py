# question 1
def combine_values(*numbers):
    if not numbers:
        return 1
    product = 1
    for number in numbers:
        product *= number
    return product 

print(combine_values(2, 3, 4)) # → 24
print(combine_values(5)) # → 5
print(combine_values()) # → 1

# question 2

def merge_details(label, **details):
    result = {"label": label}
    result.update(details)
    return result

print(merge_details("ItemA", size="Large", cost=12.50))
print(merge_details("UserX"))

# question 3
def process_data(*values, rate=2):
    if not values:
        return 0
    total = 0
    for v in values:
        total += v * rate
    return total

print(process_data(3, 1)) # 8
print(process_data(2, rate=5)) # 10
print(process_data()) # 0

# question 4
def build_record(name, **info):
    record = {"name": name}
    record.update(info)
    record["count"] = len(info)
    return record

print(build_record("Alpha", x=1, y=2)) # {"name": Alpha, "x": 1, "y": 2, "count": 2}
print(build_record("Beta")) # {"name": Beta, "count": 0} count is 0 because there are no kwargs