# # method 1
# def sanitize_filename(filename):
#     # lowercase
#     clean = filename.lower()
    
#     # spaces to underscores
#     clean = clean.replace(" ", "_")
    
#     # keep only allowed characters
#     allowed = ""
#     for char in clean:
#         if char.isalnum() or char in ".-_":
#             allowed += char
    
#     # .txt extension
#     if allowed.endswith(".txt"):
#         result = allowed
#     else:
#         if "." in allowed:
#             dos_pos = allowed.rfind(".")
#             allowed = allowed[:dos_pos]
#         result = allowed + ".txt"
        
#     # max 50 chars
#     if len(result) > 50:
#             max_base = 50 - 4 # 4 for ".txt"
#             result = result[:max_base] + ".txt"
            
#     return result

# # method 2
# def sanitize_filename(filename):

#     # lowercase and replace spaces
#     clean = filename.lower().replace(" ", "_")
    
#     # keep safe characters
#     safe = ""
#     for char in clean:
#         if char.isalnum() or char in ".-_":
#             safe += char
    
#     # handle extension
#     if not safe.endswith(".txt"):
#         if "." in safe:
#             safe = safe[:safe.rfind(".")]
#         safe += ".txt"
        
#     # truncate
#     if len(safe) > 50:
#         safe = safe[:46] + ".txt"
        
#     return safe

# print(sanitize_filename("Ancient Scroll.txt"))
# print(sanitize_filename("Quest 2042! (Epic)"))
# print(sanitize_filename("notes"))
# print(sanitize_filename("X"*60))

    