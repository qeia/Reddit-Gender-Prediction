import praw
import urllib, json
import collections


r = praw.Reddit(user_agent = 'sid')

file = open("male_TEST.txt","r")
file2=open("malecommentTEXT.txt","w")
b=0
c=0
for user in file:
	try:
		u=r.get_redditor(user[:-1])
	except Exception as err:
		print "deleted"
		continue	
	try:
		file2.write('%%%%'+user[:-1]+'%%%%\n')
		for comment in u.get_comments(limit=None):
			c=c+1
			file2.write(comment.body+'\n')
	except Exception as err:
		b=b+1
		print "VALUE OF A________________=",b,c
		continue	
	
file.close()   
file2.close()


r = praw.Reddit(user_agent = 'sid')

file = open("female_TEST.txt","r")
file2=open("femalecommentTEXT.txt","w")
b=0
c=0
for user in file:
	try:
		u=r.get_redditor(user[:-1])
	except Exception as err:
		print "deleted"
		continue	
	try:
		file2.write('%%%%'+user[:-1]+'%%%%\n')
		for comment in u.get_comments(limit=None):
			
			c=c+1
			file2.write(comment.body+'\n')
	except Exception as err:
		b=b+1
		print "VALUE OF A________________=",b,c
		continue	
	
file.close()   
file2.close()