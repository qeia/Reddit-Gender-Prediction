from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
f=open("malecomment3.txt","r")
f1=open("femalecomment3.txt","r")
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split

data = []
d1=[]
target=[]
from sklearn.feature_extraction.text import TfidfTransformer
for line in f:
	
	

	
	if "%%%%" == line[:4]:
		data.append(' '.join(d1))
		target.append('m')
		d1=[]
		user = line[4:][:-4]
		
		continue
	d1.append(line)	
print len(data)


d1=[]
for line in f1:
	
	
	
	if "%%%%" == line[:4]:
		target.append('f')
		data.append(' '.join(d1))
		d1=[]
		user = line[4:][:-4]
		
		continue
	d1.append(line)
X_train = data
print X_train_counts.shape
f.close()
f1.close()

tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
print len(target)
print X_train_tf.shape
text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB()),])
text_clf = text_clf.fit(twenty_train.data, twenty_train.target)
text_clf.score(X_train)

