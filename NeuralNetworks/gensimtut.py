f=open("malecomments_final.txt","r")
f1=open("femalecomments_final.txt","r")
data = []
d1=[]
target=[]
from gensim.parsing.preprocessing import STOPWORDS
s=set(STOPWORDS)
s.update(["it","don't","i'm","you're","like","it's","people","good","know","they're","going","can't"])
from nltk.corpus import stopwords

import gensim
from gensim import corpora
c=0
for line in f:
	
	c+=1

	
	if "%%%%" == line[:4]:
		if c==1:
			continue
		data.append(' '.join(d1).replace('\n', ''))
		target.append('m')
		
		d1=[]
		user = line[4:][:-4]
		
		continue
	if len(d1)<100:	
		d1.append(line)	
	if len(data)>500:
		break	
length1=len(data)	
print "num of male",len(data)
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
	if len(d1)<100:	
		d1.append(line)	
	if len(data)>1000:
		break	
print "num of female",len(data)-length1
count  = 0
documents=data
f.close()
f1.close()
texts = [[word for word in document.lower().split() if word not in stopwords.words('english')] for document in documents]
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
	for token in text:
		frequency[token] += 1
texts = [[token for token in text if frequency[token] > 1] for text in texts]		
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=100)
lda.print_topics(num_topics=20, num_words=10)
a=lda.print_topics(num_topics=20, num_words=10)
print a