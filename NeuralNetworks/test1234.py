from sklearn.feature_extraction.text import CountVectorizer
from nltk import word_tokenize          
from nltk.stem.porter import PorterStemmer
import nltk

stemmer = PorterStemmer()
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems
count_vect = CountVectorizer(stop_words='english')
f=open("malecomment4.txt","r")
f1=open("femalecomment4.txt","r")
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
data = []
d1=[]
target=[]
from sklearn.feature_extraction.text import TfidfTransformer
for line in f:
	
	

	
	if "%%%%" == line[:4]:

		data.append(' '.join(d1).replace('\n', ''))
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
X_train=data
X_train_counts = count_vect.fit_transform(X_train)
count  = 0


f.close()
f1.close()

tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
print type(X_train_counts)
