import json
import praw

from pprint import pprint
r = praw.Reddit(user_agent = 'sid')
content = []
with open('male.txt') as f:
    content = f.readlines()
dict2 = {}
content2= content[0:25]
n=0
for cont in content2:
    user = r.get_redditor(cont)
    gen = user.get_comments(limit =None)

    dict = {}

    for com in gen:
        if dict.has_key(str(com.subreddit.display_name)) is False:
            dict[str(com.subreddit.display_name)]=1
        else:
            dict[str(com.subreddit.display_name)]+=1


    dict2[str(user)]=dict
    n=n+1
    print n

with open('male.json', 'w') as f:
    json.dump(dict2, f)

content = []
with open('female.txt') as f:
    content = f.readlines()
dict2 = {}
content2= content[0:25]
for cont in content2:
    user = r.get_redditor(cont)
    gen = user.get_comments(limit =None)

    dict = {}

    for com in gen:
        if dict.has_key(str(com.subreddit.display_name)) is False:
            dict[str(com.subreddit.display_name)]=1
        else:
            dict[str(com.subreddit.display_name)]+=1

    dict2[str(user)]=dict
    n=n+1
    print n

with open('female.json', 'w') as f:
    json.dump(dict2, f)
