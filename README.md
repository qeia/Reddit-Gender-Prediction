Predicted gender of Reddit users based on his/her comments using SVM.

Firstly, I used reddit API to mine comments. I used /r/askmen and /r/askwomen for getting male and female data. These subreddits
inlcuded flairs for gender and I used these flairs to segregate the male and female users.

After getting male and female usernames, I mined their comments and made 2 files, malecomments.txt and femalecomments.txt.

Then  I used SVM from Sciki-Learn to predict the gender. I used SVM since the data was sparse and SVM seems to work well with text data. 

The features used were in the form of bag of words. I tried using 2-gram of words but it took too much time and the accuracy reduced anyway.

I also tried latent dirichlet allocation but scikit-learn's algorithm seems to be buggy.

I split the data into test and train by 40% propotion. I could then obtain 87% accuracy. 

Interestingly, these are the top scoring words for males and females.

	-2.3321	love           		1.8457	man            
	-2.1995	boyfriend      		1.3747	game           
	-2.0318	husband        		1.3209	wife           
	-1.7239	really         		1.2557	girlfriend     
	-1.3975	thank          		1.1922	shit           
	-1.3542	hair           		1.1346	fuck           
	-1.2402	baby           		1.0311	girl           
	-1.2175	feel           		1.0020	https          
	-1.1905	skin           		0.9633	youtube        
	-1.1852	family         		0.9513	guy            
	-1.1818	mom            		0.9474	team           
	-1.1597	wear           		0.9433	dude           
	-1.1533	definitely     		0.9210	gf             
	-1.1464	makeup         		0.9140	point          
	-1.0623	super          		0.9036	right          
	-1.0565	pregnant       		0.8812	dick           
	-1.0136	cute           		0.8734	car            
	-1.0136	askwomen       		0.8574	good           
	-0.9958	yes            		0.8448	hit            
	-0.9684	like           		0.8361	10 
