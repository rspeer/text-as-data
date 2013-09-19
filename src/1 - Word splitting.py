# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from __future__ import unicode_literals

# <codecell>

text = '''"Words," you might say, "are things separated by spaces."'''

# <codecell>

for word in text.split(' '):
    print word

# <codecell>

text2 = '''Okay, words are sequences of letters that don't include punctuation.'''

# <codecell>

import re
for word in re.findall(r'[A-Za-z]+', text2):
    print word

# <codecell>

text3 = '''Isn't it naïve to not include the apostrophe?'''

# <codecell>

for word in re.findall(r"[A-Za-z']+", text3):
    print word

# <codecell>

text4 = "Fine, let's use NLTK. That shouldn't be too hard."

# <codecell>

import nltk

# <codecell>

for sent in nltk.sent_tokenize(text4):
    print
    for word in nltk.word_tokenize(sent):
        print word

# <codecell>

from nltk.corpus import wordnet

# <codecell>

text2 = "You might be wondering whether we can deal with suffixes"
for word in nltk.word_tokenize(text2):
    word = word.lower()
    print wordnet.morphy(word) or word

# <codecell>


