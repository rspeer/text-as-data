
In[3]:

```
from nltk.book import *
```


    *** Introductory Examples for the NLTK Book ***
    Loading text1, ..., text9 and sent1, ..., sent9
    Type the name of the text or sentence to view it.
    Type: 'texts()' or 'sents()' to list the materials.
    text1: Moby Dick by Herman Melville 1851
    text2:

In[4]:

```
import nltk
```

In[5]:

```
nltk.bigrams(text1[4712:4732])
```




    [('Call', 'me'),
     ('me', 'Ishmael'),
     ('Ishmael', '.'),
     ('.', 'Some'),
     ('Some', 'years'),
     ('years', 'ago'),
     ('ago', '--'),
     ('--', 'never'),
     ('never', 'mind'),
     ('mind', 'how'),
     ('how', 'long'),
     ('long', 'precisely'),
     ('precisely', '--'),
     ('--', 'having'),
     ('having', 'little'),
     ('little', 'or'),
     ('or', 'no'),
     ('no', 'money'),
     ('money', 'in')]



In[6]:

```
text1.collocations()
```


    Building collocations list
    Sperm Whale; Moby Dick; White Whale; old man; Captain Ahab; sperm
    whale; Right Whale; Captain Peleg; New Bedford; Cape Horn; cried Ahab;
    years ago; lower jaw; never mind; Father Mapple; cried Stubb; chief
    mate; white whale; ivory leg; one hand


In[7]:

```
text3.collocations()
```


    Building collocations list
    said unto; pray thee; thou shalt; thou hast; thy seed; years old;
    spake unto; thou art; LORD God; every living; God hath; begat sons;
    seven years; shalt thou; little ones; living creature; creeping thing;
    savoury meat; thirty years; every beast


In[8]:

```
text2.collocations()
```


    Building collocations list
    Colonel Brandon; Sir John; Lady Middleton; Miss Dashwood; every thing;
    thousand pounds; dare say; Miss Steeles; said Elinor; Miss Steele;
    every body; John Dashwood; great deal; Harley Street; Berkeley Street;
    Miss Dashwoods; young man; Combe Magna; every day; next morning


In[9]:

```
text6.collocations()
```


    Building collocations list
    BLACK KNIGHT; HEAD KNIGHT; Holy Grail; FRENCH GUARD; Sir Robin; Run
    away; CARTOON CHARACTER; King Arthur; Iesu domine; Pie Iesu; DEAD
    PERSON; Round Table; OLD MAN; dramatic chord; dona eis; eis requiem;
    LEFT HEAD; FRENCH GUARDS; music stops; Sir Launcelot


In[10]:

```
# Make a frequency distribution.
# It maps the first two words in a trigram to a
# distribution of what the third word could be.
cfd = nltk.ConditionalFreqDist(
    ((first, second), third)
    for first, second, third in nltk.trigrams(text6)
)
```

In[11]:

```
# Generate text by repeatedly adding the most likely
# word given the previous two.
def generate_words(cfdist, word1, word2, num=30):
    print word1,
    for i in range(num):
        print word2,
        next = cfdist[word1, word2].max()
        word1, word2 = word2, next
```

In[12]:

```
generate_words(cfd, 'KING', 'ARTHUR')
```


    KING ARTHUR : What is your name ? TIM : I ' m not dead ! [ clang ] Bring out your dead ! [ clang ] Bring out your dead


In[ ]:

```

```
