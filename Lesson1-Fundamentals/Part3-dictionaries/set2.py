def calculate_engagement_rate(post):
    views = post.get("views", 0)
     
    if views == 0:
        return 0
    
    likes = post.get("likes", 0)
    comments = post.get("comments", 0)
    shares = post.get("shares", 0)
    
    engagement = likes + comments + shares
    rate = ( engagement / views )
    pass



post = {"views": 1000, "Likes": 50, "comments": 10, "shares": 5}
print(calculate_engagement_rate(post))

