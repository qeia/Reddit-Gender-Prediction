import json
from pprint import pprint

with open('1female.json') as data_file:    
    data = json.load(data_file)


x = data[1]["data"]["children"]
da = []
i = 0
for a in x:
	
	if "author_flair_css_class" in a["data"] and a["data"]["author_flair_css_class"] == "female":
		da.append(a["data"]["author"])
	for keys in a["data"].keys():
		print keys

print da
