announcement = " BERGEN TECH robotics meeting TODAY! "

def format_course_code(code):
  #  trimmed = code.strip()
  #  print(f"After strip: {trimmed}")
    
  #  uppercased = trimmed.upper()
  #  print(f"After upper: {uppercased}")
    
   # return uppercased

    return code.strip().upper()

print(format_course_code(" BERGEN TECH robotics meeting TODAY! "))

def count_hastags(post):
   # hashtag_count = 0
   # for hashtags in post:
   #     if hashtags == "#":
   #         hashtag_count += 1
  #  return hashtag_count
    
    # method 2 (preferred methid)
    words = post.split()
    count = 0
    for word in words:
        if word.startswith("#"):
            count += 1
            
    return count
    
post1 = "Great game today! #BergenTech #GoGamez #Pride"

print(count_hastags(post1))

# endswith()

