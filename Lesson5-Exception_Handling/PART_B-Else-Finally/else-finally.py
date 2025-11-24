try:
    # try something risky
    score = int(input("Enter score: "))
    
except ValueError:
    # runs if it failed
    print("Invalid score")
    
else: 
# runs if it succeeded 
    print(f"score recorded {score}")
    


def parse_command(message):
    """Parse a discord command like: !ban PlayerName 7days"""
    try:
        parts = message.split()
        command = parts[0]
        target = parts[1]
        duration = parts[2]
        
    except IndexError:
        print("❌ invalid command format: missing parts!")
        return None
    
    else:
        print("✅ command parsed succesful")
        if command.startswith("!"):
            print(f"⚡️ Executing {command}")
        return command, target, duration
    finally: # runs no matter what
        print("This block runs regardless!")
    
print(parse_command("!ban PlayerName 7days"))
print(parse_command(""))