from sklearn.feature_extraction.text import CountVectorizer
from nltk import word_tokenize          
from nltk.stem import WordNetLemmatizer 

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
X_train, X_test, y_train, y_test = train_test_split(data,target, test_size=0.4, random_state=3)
X_train_counts = count_vect.fit_transform(X_train)
count  = 0


f.close()
f1.close()

tf_transformer = TfidfTransformer(use_idf=True).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
print len(target)
print X_train_tf.shape
text_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),('tfidf', TfidfTransformer(use_idf=True)),
	('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, n_iter=12, random_state=42))])

x1 = text_clf.fit(X_train, y_train)
print text_clf.score(X_test,y_test)
def most_informative_feature_for_binary_classification(vectorizer, classifier, n=10):
    class_labels = classifier.named_steps['clf'].classes_
    feature_names = vectorizer.get_feature_names()
    topn_class1 = sorted(zip(classifier.named_steps['clf'].coef_[0], feature_names))[:n]
    topn_class2 = sorted(zip(classifier.named_steps['clf'].coef_[0], feature_names))[-n:]

    for coef, feat in topn_class1:
        print class_labels[0], coef, feat

    print

    for coef, feat in reversed(topn_class2):
        print class_labels[1], coef, feat


print most_informative_feature_for_binary_classification(count_vect, text_clf)
def show_most_informative_features(vectorizer, clf, n=20):
    feature_names = vectorizer.get_feature_names()
    coefs_with_fns = sorted(zip(clf.named_steps['clf'].coef_[0], feature_names))
    top = zip(coefs_with_fns[:n], coefs_with_fns[:-(n + 1):-1])
    for (coef_1, fn_1), (coef_2, fn_2) in top:
        print "\t%.4f\t%-15s\t\t%.4f\t%-15s" % (coef_1, fn_1, coef_2, fn_2)
print show_most_informative_features(count_vect,text_clf) 
#import cPickle
#with open('Gender_Classifier.pkl', 'wb') as fid:
#    cPickle.dump(x1, fid)



