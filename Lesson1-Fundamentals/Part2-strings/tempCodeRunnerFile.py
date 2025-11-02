# method 1
def sanitize_filename(filename):
    # lowercase
    clean = filename.lower()
    
    # spaces to underscores
    clean = clean.replace(" ", "_")
    
    # keep only allowed characters
    allowed = ""
    for char in clean:
        if char.alnum() or char in ".-_":
            allowed += char
    
    # .txt extension
    if allowed.endswith(".txt"):
        result = allowed
    else:
        if "." in allowed:
            dos_pos = allowed.rfind(".")
            allowed = allowed[:dos_pos]
        result = allowed + ".txt"
        
        # max 50 chars
        if len(result > 50):
            max_base = 50 - 4 # 4 for ".txt"
            result = result[:max_base] + ".txt"
            result = result[:max_base] + ".txt"
            
        return result