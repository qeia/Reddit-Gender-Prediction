file = open("female5.txt","r")
d=[]
for a in file:
	d.append(a)
if len(d) != len(set(d)):
	print x
print d	