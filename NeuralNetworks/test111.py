import praw
import urllib, json
import collections



file = open("female5.txt","r")
for user in file:
	print user[:-1]

for bla in xrange(len(X_train_counts)):
	if X_train_counts[bla] == 1:
		count=count+1	