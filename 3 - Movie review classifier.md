
In[1]:

```
import nltk
from nltk.corpus import movie_reviews
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
import numpy as np
import random
```

In[2]:

```
# Get a list of (document text, category)
documents = [
    (movie_reviews.raw(fileid), category)
    for category in movie_reviews.categories()
    for fileid in movie_reviews.fileids(category)
]
random.seed(3)
random.shuffle(documents)
```

In[3]:

```
documents[0]
```




    (' " stuart little " is one of the best family films to come out this year . \nit\'s a cute , funny and very good-natured film that has nothing for parents to squirm over except a few mild cusswords . \nthough i read the book a long time ago and i really do not remember what it was about , i do know that this film does not disappoint . \nfinally a movie gets released that is as good as the trailer makes it to be , with a few surprising twists , some very funny moments , and a few sentimental moments all mixed in to one great little movie . \nstuart little is a mouse . \nhe has finally gotten a new home after being put up for adoption , he now lives with the littles . \na nice little ( no pun intended ) family that lives in their apartment next to central park in new york city . \nthey have a little boy george ( played by the adorable jonathan lipnicki ) and now they have a new son . \nat first stuart takes a while but he finally adjusts to being part of the family and even getting along with the pet cat . \ngeorge doesn\'t take too well to having a mouse for a brother at first , but once the two play together they instantly bond . \nstuart however is missing something , and he wants to know who his real parents are . \nthe littles try and find his parents and one day they show up on the doorstep wanting stuart back . \nhesitating the littles know what\'s best for stuart and so does snowball the pet cat , he and his friends try to get stuart but in the end we find out the truth about stuart\'s past ending up to a sentimental and very heart-warming ending . \none thing i noticed about the film instantly was the fantastic special effects . \njust like in " star wars : episode 1--the phantom menace " stuart little and his family are all computer generated and they look fantastically real . \nfrom the detail of their fur , to the detail of the way the walk ; the special effects team put a lot of time and effort on this $90 million dollar film and it shows . \nanother movie that this has in common with is " babe " with it\'s talking animals and people understanding them . \nit has a family friendly atmosphere and is never really scary or suspenseful enough to even scare the youngest of kids . \nmichael j . fox does the voice of stuart himself and just like in the " homeward bound " movies does a fantastic job and brings more out of stuart than anyone else could . \nhe to me fits the character perfectly and ends up making stuart even more lovable . \nanother gem of the film is nathan lane as snowball . \nwhen he was timon in 1994\'s " the lion king " i would have sworn he was a comedian , and now in " stuart little " he brings the most out of snowball and makes him one of those characters we love to dislike . \nfor the human actors geena davis who never gives a bad performance does not disappoint here as well . \nshe fits nicely in her character and there is a good chemistry between her and hugh laurie who plays mr . little . \nboth make us believe they are happily in love and married and jonathan lipnicki as their song is even more adorable than he was in 1996\'s " jerry maguire " . \neven though stuart little is completely cgi , the human characters and stuart have a nice chemistry together and even makes us believe they really do care for each other . \n " stuart little " is ideal family entertainment for this holiday season and will not disappoint youngsters or adults for that matter . \nwe get entertainment , laughs , cries and more fun at the movies this season than probably any other movie . \nits nice to see a pg rated movie out at christmas that everyone can see . \neven though it has a $90 million dollar budget i\'m sure it will make over that or just below it respectively . \nfor all you parents out there trying to find a good family movie , i have yet to see bicentennial man as i write this but as far as i know " stuart little " and " toy story 2 " are by far the best family films this year . \na winner . ? \n',
     'pos')



In[4]:

```
train_samples, test_samples = documents[:1000], documents[1000:]
```

In[5]:

```
# Make feature vectors out of the documents, based on which words they contain
vectorizer = CountVectorizer(binary=True)
train_vectors = vectorizer.fit_transform([doc for doc, target in train_samples])
test_vectors = vectorizer.transform([doc for doc, target in test_samples])
train_targets = [target for doc, target in train_samples]
test_targets = [target for doc, target in test_samples]
```

In[6]:

```
classifier = BernoulliNB()
```

In[7]:

```
classifier.fit(train_vectors, train_targets)
```




    BernoulliNB(alpha=1.0, binarize=0.0, class_prior=None, fit_prior=True)



In[8]:

```
# A helper function to see which features affect the classification the most
def show_most_informative_features(vectorizer, classifier, n=10):
    neg = classifier.feature_log_prob_[0]
    pos = classifier.feature_log_prob_[1]
    valence = (pos - neg)
    ordered = np.argsort(valence)
    interesting = np.hstack([ordered[:n], ordered[-n:]])
    feature_names = vectorizer.get_feature_names()
    for index in ordered[:n]:
        print "%+4.4f\t%s" % (valence[index], feature_names[index])
    print '\t...'
    for index in ordered[-n:]:
        print "%+4.4f\t%s" % (valence[index], feature_names[index])
    
```

In[9]:

```
show_most_informative_features(vectorizer, classifier)
```


    -3.0751	ludicrous
    -2.4690	unwatchable
    -2.4690	seagal
    -2.4690	idiotic
    -2.3820	3000
    -2.2866	recycled
    -2.2866	spouting
    -2.2866	subway
    -2.2866	degenerates
    -2.2866	stupidity
    	...
    +2.3185	atlantic
    +2.3831	outstanding
    +2.4138	goodfellas
    +2.4138	lush
    +2.4138	farther
    +2.4138	poker
    +2.4583	breathtaking
    +2.5008	gripping
    +2.5008	animators
    +2.6550	finest


In[10]:

```
classifier.score(test_vectors, test_targets)
```




    0.79800000000000004



In[ ]:

```

```
