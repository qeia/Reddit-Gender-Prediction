Predicted gender of Reddit users based on his/her comments using SVM.

Firstly, I used reddit API to mine comments. I used /r/askmen and /r/askwomen for getting male and female data. These subreddits
inlcuded flairs for gender and I used these flairs to segregate the male and female users.

After getting male and female usernames, I mined their comments and made 2 files, malecomments.txt and femalecomments.txt.

Then  I used SVM from Sciki-Learn to predict the gender. I used SVM since the data was sparse and SVM seems to work well with text data. 

The features used were in the form of bag of words. I tried using 2-gram of words but it took too much time and the accuracy reduced anyway.

I also tried latent dirichlet allocation but scikit-learn's algorithm seems to be buggy.

I split the data into test and train by 40% propotion. I could then obtain 87% accuracy. 
