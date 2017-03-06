from sklearn.feature_extraction.text import CountVectorizer
from nltk import word_tokenize          
from nltk.stem import WordNetLemmatizer 
from sklearn.decomposition import NMF, LatentDirichletAllocation
import numpy as np

def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print "Topic #%d:" % topic_idx
        print " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
    


f=open("malecomments_final.txt","r")
f1=open("femalecomments_final.txt","r")
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier		
count_vect = CountVectorizer(stop_words='english') 		
data = []
d1=[]
target=[]
c=0
from sklearn.feature_extraction.text import TfidfTransformer
for line in f:
	
	

	c+=1
	if "%%%%" == line[:4]:
		if c==1:
			continue
		data.append(' '.join(d1))
		target.append('m')
		
		d1=[]
		user = line[4:][:-4]
		
		continue
	d1.append(line)	
length1=len(data)	
print len(data)
d1=[]
c=0
for line in f1:
	
	
	c+=1
	if "%%%%" == line[:4]:
		if c==1:
			continue
		target.append('f')
		data.append(' '.join(d1))
		d1=[]
		user = line[4:][:-4]
		
		continue
	d1.append(line)
print len(data)-length1
X_train, X_test, y_train, y_test = train_test_split(data,target, test_size=0.1, random_state=3)
X_train1, X_test1, y_train1, y_test1 = train_test_split(data,target, test_size=0.4, random_state=3)
X_train2, X_test2, y_train2, y_test2 = train_test_split(data,target, test_size=0.6, random_state=3)
X_train3, X_test3, y_train3, y_test3 = train_test_split(data,target, test_size=0.8, random_state=20)
X_train_counts = count_vect.fit_transform(X_train)
X_train_counts3=count_vect.fit_transform(X_train3)
count  = 0


f.close()
f1.close()
tf_transformer3 = TfidfTransformer(use_idf=True).fit(X_train_counts3)
tf_transformer = TfidfTransformer(use_idf=True).fit(X_train_counts)

X_train_tf = tf_transformer.transform(X_train_counts)
tf_transformer=TfidfTransformer(use_idf=True).fit()

import cPickle
with open('tf_transformer.pkl', 'wb') as fid:
    cPickle.dump(tf_transformer, fid)    
with open('X_train_tf.pkl', 'wb') as fid:
    cPickle.dump(X_train_tf,fid) 
with open('count_vect.pkl', 'wb') as fid:
    cPickle.dump(count_vect,fid)     