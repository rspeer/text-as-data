
In[1]:

```
import nltk
from nltk.corpus import movie_reviews
import numpy as np
```

In[2]:

```
documents = [
    list(movie_reviews.words(fileid))
    for category in movie_reviews.categories()
    for fileid in movie_reviews.fileids(category)
]
```

In[3]:

```
print ' '.join(documents[1])
```


    the happy bastard ' s quick movie review damn that y2k bug . it ' s got a head start in this movie starring jamie lee curtis and another baldwin brother ( william this time ) in a story regarding a crew of a tugboat that comes across a deserted russian tech ship that has a strangeness to it when they kick the power back on . little do they know the power within . . . going for the gore and bringing on a few action sequences here and there , virus still feels very empty , like a movie going for all flash and no substance . we don ' t know why the crew was really out in the middle of nowhere , we don ' t know the origin of what took over the ship ( just that a big pink flashy thing hit the mir ) , and , of course , we don ' t know why donald sutherland is stumbling around drunkenly throughout . here , it ' s just " hey , let ' s chase these people around with some robots " . the acting is below average , even from the likes of curtis . you ' re more likely to get a kick out of her work in halloween h20 . sutherland is wasted and baldwin , well , he ' s acting like a baldwin , of course . the real star here are stan winston ' s robot design , some schnazzy cgi , and the occasional good gore shot , like picking into someone ' s brain . so , if robots and body parts really turn you on , here ' s your movie . otherwise , it ' s pretty much a sunken ship of a movie .


In[5]:

```
from gensim import models, similarities, corpora
```

In[6]:

```
dictionary = corpora.Dictionary(documents)
corpus = [dictionary.doc2bow(text) for text in documents]
```

In[7]:

```
len(dictionary), len(corpus)
```




    (39768, 2000)



In[8]:

```
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=50)
```

In[9]:

```
# Gives us an object where we put in an appropriate reduced
# bag of words, and it gives us similarity over all documents
similarity = similarities.MatrixSimilarity(lsi[corpus])
```

In[10]:

```
# A useful function for looking at what's going on.
#
# It takes in a vector of how similar N things are to some input.
# It also takes a 'display_func' to tell it how to show you what
# those N things actually are.
def show_similar(similarities, display_func):
    best_matches = np.argsort(similarities)[::-1][:10]
    for index in best_matches:
        print "%4.4f\t%s" % (similarities[index], display_func(index))
```

In[11]:

```
# Here's a way to get a similarity vector.
def doc_similarities(doc):
    bag_of_words = dictionary.doc2bow(doc)
    return similarity[lsi[bag_of_words]]
```

In[12]:

```
# And here's the display_func we'll need.
def brief_document(index):
    doc = documents[index]
    return ' '.join(doc)[:200] + '...'
```

In[13]:

```
show_similar(doc_similarities(documents[1]), brief_document)
```


    1.0000	the happy bastard ' s quick movie review damn that y2k bug . it ' s got a head start in this movie starring jamie lee curtis and another baldwin brother ( william this time ) in a story regarding a cr...
    0.9629	if you ' re the kind of person who goes to see movies just because you long for some of that overpriced theatre popcorn ( butter optional ) , then this is the movie for you ! indeed , this has got to ...
    0.9422	this movie tries to present itself as the sequel to jan de bont ' s debut as a director , 1994 surprise hit speed . but the only thing the two movies have in common is sandra bullock as the female lea...
    0.9387	isn ' t it the ultimate sign of a movie ' s cinematic ineptitude when you can ' t think of much to say about it other than " it sucks " ? one of the first official year 2000 releases , supernova is su...
    0.9383	the most interesting thing about virus is that the title of the film does not refer to the clunky robotic animals that try to kill our heroes . alas , it refers to our heroes ! as it turns out , the a...
    0.9345	the formula is simple . trap a varied group of people on an isolated location , then pop in a seemingly unstoppable monster to kill them one by one . these have been the successful ingredients for man...
    0.9301	deep rising is one of " those " movies . the kind of movie which serves no purpose except to entertain us . it does not ask us to think about important questions like life on other planets or the poss...
    0.9238	there may not be a critic alive who harbors as much affection for shlock monster movies as i do . i delighted in the sneaky - smart entertainment of ron underwood ' s big - underground - worm yarn tre...
    0.9233	welcome to your oh - so typical sequel . it tries to be twice as big as it ' s predecessor , yet ends up twice as shallow . shallow . . . . hmm . . . now there ' s an idea . maybe if the ill - fated c...
    0.9222	here ' s something to chew on : what ' s the favorite food of big , cheesy - looking special effects monsters like the one lurking in the bowels of a luxury liner in deep rising ? the obvious answer t...


In[14]:

```
def term_similarities(term):
    return lsi.projection.u.dot(lsi.projection.u[dictionary.token2id[term]])
```

In[15]:

```
show_similar(term_similarities('boat'), lambda x: dictionary.id2token[x])
```


    0.0257	ship
    0.0210	titanic
    0.0140	joe
    0.0124	godzilla
    0.0102	cameron
    0.0102	virus
    0.0091	rose
    0.0085	--
    0.0082	rising
    0.0079	spielberg


In[16]:

```
show_similar(term_similarities('alien'), lambda x: dictionary.id2token[x])
```


    0.3406	alien
    0.2193	ripley
    0.1851	aliens
    0.0884	species
    0.0584	fincher
    0.0579	weaver
    0.0480	
    0.0480	3
    0.0438	resurrection
    0.0423	patrick


In[17]:

```
show_similar(term_similarities('good'), lambda x: dictionary.id2token[x])
```


    0.0110	patch
    0.0098	melvin
    0.0089	lambeau
    0.0085	murphy
    0.0084	hunting
    0.0083	i
    0.0078	good
    0.0076	action
    0.0071	bad
    0.0068	really


In[ ]:

```

```
