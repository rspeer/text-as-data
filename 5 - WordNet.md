
In[1]:

```
from nltk.corpus import wordnet as wn
```

In[2]:

```
[(synset, synset.definition) for synset in wn.synsets('dog')]
```




    [(Synset('dog.n.01'),
      'a member of the genus Canis (probably descended from the common wolf) that has been domesticated by man since prehistoric times; occurs in many breeds'),
     (Synset('frump.n.01'), 'a dull unattractive unpleasant girl or woman'),
     (Synset('dog.n.03'), 'informal term for a man'),
     (Synset('cad.n.01'), 'someone who is morally reprehensible'),
     (Synset('frank.n.02'),
      'a smooth-textured sausage of minced beef or pork usually smoked; often served on a bread roll'),
     (Synset('pawl.n.01'),
      'a hinged catch that fits into a notch of a ratchet to move a wheel forward or prevent it from moving backward'),
     (Synset('andiron.n.01'), 'metal supports for logs in a fireplace'),
     (Synset('chase.v.01'), 'go after with the intent to catch')]



In[3]:

```
dog = wn.synset('dog.n.01')
cat = wn.synset('cat.n.01')
toaster = wn.synset('toaster.n.01')
```

In[4]:

```
wn.wup_similarity(dog, cat)
```




    0.8571428571428571



In[5]:

```
wn.wup_similarity(cat, toaster)
```




    0.5



In[6]:

```
wn.morphy('dogs'), wn.morphy('barked')
```




    ('dog', 'bark')



In[7]:

```
[(synset, synset.definition) for synset in wn.synsets('bark')]
```




    [(Synset('bark.n.01'),
      'tough protective covering of the woody stems and roots of trees and other woody plants'),
     (Synset('bark.n.02'), 'a noise resembling the bark of a dog'),
     (Synset('bark.n.03'), 'a sailing ship with 3 (or more) masts'),
     (Synset('bark.n.04'), 'the sound made by a dog'),
     (Synset('bark.v.01'), 'speak in an unfriendly tone'),
     (Synset('bark.v.02'), 'cover with bark'),
     (Synset('bark.v.03'), 'remove the bark of a tree'),
     (Synset('bark.v.04'), 'make barking sounds'),
     (Synset('bark.v.05'), 'tan (a skin) with bark tannins')]



In[8]:

```
print wn.wup_similarity(wn.synset('dog.n.01'), wn.synset('bark.n.04'))
```


    0.117647058824


In[ ]:

```

```
