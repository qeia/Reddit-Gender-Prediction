import json
from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer
import pickle
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
print subreddit[0]
ind=subreddit.index("TwoXChromosomes")

print subreddit
#male part of organizing
male_array = []
l=len(subreddit)
for male in male_dict.iterkeys():
    m = [0]*l
    tempdict = male_dict[male]
    for sub in tempdict.iterkeys():
         m[subreddit.index(sub)]=tempdict[sub]
    male_array.append(m)

female_array=[]
for female in female_dict.iterkeys():
    f = [0]*l
    tempdict = female_dict[female]
    for sub in tempdict.iterkeys():
         f[subreddit.index(sub)]=tempdict[sub]
    female_array.append(f)
#neural network here
alldata = ClassificationDataSet(len(subreddit), 1, nb_classes=2)
for m in male_array:
    alldata.addSample(m,[0])
    print m

for f in female_array:
    print f
    alldata.addSample(f,[1])
count = 0
for f in female_array:
    count=count+ f[ind]
    print count
count = 0
for m in male_array:
    count=count+ m[ind]
    print count
alldata._convertToOneOfMany( )

print "Number of training patterns: ", len(alldata)
print "Input and output dimensions: ", alldata.indim, alldata.outdim
print "First sample (input, target, class):"
print alldata['input'][3], alldata['target'][3], alldata['class'][15]

fnn = buildNetwork( alldata.indim, 50, alldata.outdim, outclass=SoftmaxLayer )
trainer = BackpropTrainer(fnn, dataset=alldata, momentum=0.1, verbose=True, weightdecay=0.01)
trainer.trainUntilConvergence(dataset=alldata,verbose = True, validationProportion = 0.15, maxEpochs = 1000, continueEpochs = 30)
#for i in range(20):
#    trainer.trainEpochs(2)


#test
import praw
r = praw.Reddit(user_agent = 'sid')
user = r.get_redditor('Envia')
gen = user.get_comments(limit =None)

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
fil = open("fnn","w")
a =[]
a.append(fnn)
a.append(l)
pickle.dump(a,fil)
fil.close()

print fnn.activate(testdata)
