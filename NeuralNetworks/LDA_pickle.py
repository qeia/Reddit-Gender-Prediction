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



print X_train_tf.shape
lda = LatentDirichletAllocation(n_topics=40, max_iter=20,
                                learning_method='online',
                                learning_offset=50.,
                                random_state=0)
lda.fit(X_train_tf)
X_train_counts_feature_names = count_vect.get_feature_names()
print_top_words(lda, X_train_counts_feature_names, 100)