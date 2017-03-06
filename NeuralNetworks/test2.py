import json
from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer
import pickle
import praw
fil = open('fnn','r')
a = pickle.load(fil)
fnn = a[0]
l=a[1]
r = praw.Reddit(user_agent = 'sid')
user = r.get_redditor('advai_ta')
gen = user.get_comments(limit =None)
male_dict = {}
with open('male.json') as f:
    male_dict = json.load(f)
subreddit1= []
for men in male_dict.iterkeys():
    temp=male_dict[men].keys()
    subreddit1 = subreddit1 + temp


#print subreddit1
female_dict = {}
with open('female.json') as f:
    female_dict = json.load(f)
subreddit2= []
for women in female_dict.iterkeys():
    temp=female_dict[women].keys()
    subreddit2 = subreddit2 + temp

subreddit = subreddit1 +subreddit2
subreddit.sort()
ind=subreddit.index("TwoXChromosomes")
#male part of organizing
male_array = []
l=len(subreddit)
dict = {}

for com in gen:
    if dict.has_key(str(com.subreddit.display_name)) is False:
        dict[str(com.subreddit.display_name)]=1
    else:
        dict[str(com.subreddit.display_name)]+=1


testdata = [0]*l
for sub in dict.iterkeys():
    if sub in subreddit:
        testdata[subreddit.index(sub)]=dict[sub]

print fnn.activate(testdata)
