import praw

r = praw.Reddit(user_agent = 'sid')
male = []
all_comments = r.get_comments('askmen',limit=None)
askmen = r.get_subreddit('askmen')
r1 = praw.UnauthenticatedReddit(user_agent = 's')
n=0
submissions=askmen.get_top_from_all(limit=100)
for sub in submissions:


    flat_comments = praw.helpers.flatten_tree(sub.comments)
    for comment in flat_comments:
        if not isinstance(comment, praw.objects.Comment):
            continue

        if comment.author_flair_text=='Male':
            if comment.author.name.encode('utf8')+'\n' not in male:
                male.append(comment.author.name.encode('utf8')+'\n')
                print n
                n=n+1
                if n>1000:
                    break




text_file = open("male.txt", "a")
text_file.writelines(male)
text_file.close()


print sum(1 for line in open('MALE.txt'))