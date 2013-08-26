# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from nltk.corpus import wordnet as wn

# <codecell>

[(synset, synset.definition) for synset in wn.synsets('dog')]

# <codecell>

dog = wn.synset('dog.n.01')
cat = wn.synset('cat.n.01')
toaster = wn.synset('toaster.n.01')

# <codecell>

wn.wup_similarity(dog, cat)

# <codecell>

wn.wup_similarity(cat, toaster)

# <codecell>

wn.morphy('dogs'), wn.morphy('barked')

# <codecell>

[(synset, synset.definition) for synset in wn.synsets('bark')]

# <codecell>

print wn.wup_similarity(wn.synset('dog.n.01'), wn.synset('bark.n.04'))

# <codecell>


