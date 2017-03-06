import praw
import urllib, json
import collections


r = praw.Reddit(user_agent = 'sid')
female = []
fem_files = open("male5.txt","r")
f_data=[]
for x in fem_files:
	f_data.append(x[:-1])

askwomen = r.get_subreddit('askmen')
r1 = praw.UnauthenticatedReddit(user_agent = 's')
n=0
i = 0
j=0
da = []
submissions=askwomen.get_top_from_month(limit=None)
for sub in submissions:
	b = str(sub.url)
	i = i + 1
	a = b[:-1]
	a = a + ".json"
	print "ITERATION : ",i
	try:
		response = urllib.urlopen(a)
	except IOError as err:
		print "net gg"
		continue	
	data = json.loads(response.read())
	
	if type(data) is list:
		if "data" in data[1]:
			if "children" in data[1]["data"]:
				x = data[1]["data"]["children"]
	else:
		print data
		j=j+1
		print j	
		continue		
	for a in x:
	
		if "author_flair_css_class" in a["data"] and a["data"]["author_flair_css_class"] == "male":
			if a["data"]["author"] not in da:
				print a["data"]["author"]
				if a["data"]["author"] not in f_data:
					da.append(a["data"]["author"])
				else:
					print "DUPLICATE"	
		if "replies" in a["data"] and "data" in a["data"]["replies"] and "children" in a["data"]["replies"]["data"]:
			for r in a["data"]["replies"]["data"]["children"]:
				if "author_flair_css_class" in r["data"] and r["data"]["author_flair_css_class"] == "male":
					#print "x"
					if r["data"]["author"] not in da:
						print r["data"]["author"]
						if r["data"]["author"] not in f_data:
							da.append(r["data"]["author"])		
						else:
							print "DUPLICATE"
	print "length= ", len(da)
	if len(da)>1000:
		break

	#print data
	

    #flat_comments = praw.helpers.flatten_tree(sub.comments)
    #for comment in flat_comments:
    #    if not isinstance(comment, praw.objects.Comment):
    #        continue
    #    print comment.author_flair_text
    #    if comment.author_flair_text==u'\u2640':
    #        if comment.author.name.encode('utf8')+'\n' not in female:
    #            female.append(comment.author.name.encode('utf8')+'\n')
    #            print n
    #            n=n+1
    #            if n>1000:
    #               break




text_file = open("male_TEST.txt", "a")
text_file.write("\n".join(da))
text_file.close()
fem_files.close()
