# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from __future__ import unicode_literals

# <codecell>

text = '''"Word splitting shouldn't be hard," you might say. "Words are things separated by spaces."'''

# <codecell>

for word in text.split(' '):
    print word

# <codecell>

import re
for word in re.findall(r'[A-Za-z]+', text):
    print word

# <codecell>

import nltk

# <codecell>

for sent in nltk.sent_tokenize(text):
    print
    for word in nltk.word_tokenize(sent):
        print word

# <codecell>

from nltk.corpus import wordnet

# <codecell>

# Deal with suffixes
for sent in nltk.sent_tokenize(text):
    for word in nltk.word_tokenize(sent):
        word = word.lower()
        print wordnet.morphy(word) or word

# <codecell>

from metanl import english

# <codecell>

# Deal with even more suffixes
for word in english.normalize_list(text):
    print word

# <codecell>


