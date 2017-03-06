#predict
import cPickle
import praw
with open('Gender_Classifier.pkl', 'rb') as fid:
    text_clf = cPickle.load(fid)
r = praw.Reddit(user_agent = 'sid')
comments =''
user ='jnb64'
u=r.get_redditor(user)
while 1:
	try:
		i=0
		for comment in u.get_comments(limit=None):
			i=i+1
			
			comments=comments+ ' ' +comment.body
		break
	except Exception as err:
		print err
		raw_input()
		continue	
print i		
print text_clf.predict([comments])