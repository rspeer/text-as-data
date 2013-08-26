# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from __future__ import unicode_literals

# <codecell>

text = '''"Words," you might say, "are things separated by spaces."'''

# <codecell>

text.split(' ')

# <codecell>

text2 = '''Okay, words are sequences of letters that don't include punctuation.'''

# <codecell>

import re
re.findall(r'[A-Za-z]+', text2)

# <codecell>

text3 = '''Isn't it naïve to not include the apostrophe?'''

# <codecell>

re.findall(r"[A-Za-z']+", text3)

# <codecell>

text4 = "Fine, let's use NLTK. That shouldn't be too hard."

# <codecell>

import nltk

# <codecell>

[nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(text4)]

# <codecell>

text = 'この文も、言葉で構成されています'
# Translation: "This sentence is also made of words"

# <codecell>

for word in nltk.word_tokenize(text): print(word)

# <codecell>

from metanl import japanese

# <codecell>

for word in japanese.normalize_list(text): print(word)

# <codecell>

text2 = 'You might be wondering whether we can deal with suffixes in English'

# <codecell>

from metanl import english

# <codecell>

english.normalize_list(text2)

# <codecell>


