file = open("female5.txt","r")
x=file.readlines()
lines = [line.rstrip('\n') for line in x]
#print lines
vowel = 0
length = 0
num = 0
vow=0
us=0
v=0.0
def countvowels(string):
    num_vowels=0
    for char in string:
        if char in "aeiouyAEIOUY":
           num_vowels = num_vowels+1
    return num_vowels
def countunderscore(string):
    num_vowels=0
    for char in string:
        if char in "-_":
           num_vowels = num_vowels+1
    return num_vowels    
for user in lines:
	user = user.lower()
	if user.endswith("a") or user.endswith("i") or user.endswith("o") or user.endswith("u") or user.endswith("e") or user.endswith("y"):
		vowel = vowel + 1
	length = length + len(user)
	numbers = sum(c.isdigit() for c in user)
	num = num + numbers
	vow = vow + countvowels(user)
	v=v+((countvowels(user)/float(len(user))))
	us = us + countunderscore(user)
print "vowel",vowel/1384.0	
print "length",length/1384.0
print "numbers",num/1384.0
print "vow", vow/1384.0
print "us", us/1384.0
print "v",v/1384.0

file.close()
file2 = open("male5.txt","r")
x=file2.readlines()
lines = [line.rstrip('\n') for line in x]

vowel = 0
length = 0
num = 0
vow=0
us=0
v=0.0
#print lines
for user1 in lines:
	user1 = user1.lower()
	if user1.endswith("a") or user1.endswith("i") or user1.endswith("o") or user1.endswith("u") or user1.endswith("e") or user1.endswith("y"):
		vowel = vowel + 1
	length = length + len(user1)
	numbers = sum(c.isdigit() for c in user1)
	num = num + numbers

	vow = vow + countvowels(user1)
	v=v+(countvowels(user1)/float(len(user1)))
	us=us+countunderscore(user1)

print "vowels",vowel/1590.0
print "length",length/1590.0
print "numbers",num/1590.0
print "vow",vow/1590.0
print "us",us/1590.0
print "v",v/1590.0

