# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from nltk.book import *

# <codecell>

import nltk

# <codecell>

nltk.bigrams(text1[4712:4732])

# <codecell>

text1.collocations()

# <codecell>

text3.collocations()

# <codecell>

text2.collocations()

# <codecell>

text6.collocations()

# <codecell>

# Make a frequency distribution.
# It maps the first two words in a trigram to a
# distribution of what the third word could be.
cfd = nltk.ConditionalFreqDist(
    ((first, second), third)
    for first, second, third in nltk.trigrams(text6)
)

# <codecell>

# Generate text by repeatedly adding the most likely
# word given the previous two.
def generate_words(cfdist, word1, word2, num=30):
    print word1,
    for i in range(num):
        print word2,
        next = cfdist[word1, word2].max()
        word1, word2 = word2, next

# <codecell>

generate_words(cfd, 'KING', 'ARTHUR')

# <codecell>


