from sklearn.decomposition import NMF, LatentDirichletAllocation
import cPickle
import numpy as np
def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print "Topic #%d:" % topic_idx
        print " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])

with open('X_train_tf.pkl', 'rb') as fid:
    X_train_tf = cPickle.load(fid)
with open('tf_transformer.pkl', 'rb') as fid:
    tf_transformer = cPickle.load(fid) 
with open('count_vect.pkl', 'rb') as fid:
    count_vect = cPickle.load(fid)          



X_train_counts_feature_names = count_vect.get_feature_names()
b=0
for x in X_train_tf.toarray():
	b=b+1
	a=np.argsort(x)[-10:]
	print b," USER"
	for i in a:
		print X_train_counts_feature_names[i],
	print 	
	if b>1000:
		break

