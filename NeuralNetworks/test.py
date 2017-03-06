import praw
r = praw.Reddit(user_agent = 'sid')
user = r.get_redditor('RhodeDog13')
gen = user.get_comments(limit =None)

dict = {}

for com in gen:
    if dict.has_key(str(com.subreddit.display_name)) is False:
        dict[str(com.subreddit.display_name)]=1
    else:
        dict[str(com.subreddit.display_name)]+=1
print dict