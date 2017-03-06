from sklearn.feature_extraction.text import CountVectorizer
from nltk import word_tokenize          
from nltk.stem import WordNetLemmatizer 

f=open("malecomments_final.txt","r")
f1=open("femalecomments_final.txt","r")
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
class LemmaTokenizer(object):
	def __init__(self):
		self.wnl=WordNetLemmatizer()
	def __call__(self,doc):
		return [self.wnl.lemmatize(t) for t in word_tokenize(doc)]	 		
count_vect = CountVectorizer(stop_words='english',ngram_range=(1,2)) 		
data = []
d1=[]
target=[]
d=[]
from sklearn.feature_extraction.text import TfidfTransformer
for line in f:
	
	

	
	if "%%%%" == line[:4]:

		data.append(' '.join(d1).replace('\n', ''))
		target.append('m')
		
		d1=[]
		user = line[4:][:-4]
		d.append(user)
		continue
	d1.append(line)	
print len(data)
print len(set(d))

data=[]
d=[]
for line in f1:
	
	
	
	if "%%%%" == line[:4]:
		target.append('f')
		data.append(' '.join(d1))
		d1=[]
		user = line[4:][:-4]
		d.append(user)
		continue
	d1.append(line)
print len(data)
print len(set(d))