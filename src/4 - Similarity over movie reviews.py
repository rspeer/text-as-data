# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import nltk
from nltk.corpus import movie_reviews
import numpy as np

# <codecell>

documents = [
    list(movie_reviews.words(fileid))
    for category in movie_reviews.categories()
    for fileid in movie_reviews.fileids(category)
]

# <codecell>

print ' '.join(documents[1])

# <codecell>

from gensim import models, similarities, corpora

# <codecell>

dictionary = corpora.Dictionary(documents)
corpus = [dictionary.doc2bow(text) for text in documents]

# <codecell>

len(dictionary), len(corpus)

# <codecell>

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=50)

# <codecell>

# Gives us an object where we put in an appropriate reduced
# bag of words, and it gives us similarity over all documents
similarity = similarities.MatrixSimilarity(lsi[corpus])

# <codecell>

# Here's a way to get a similarity vector.
def doc_similarities(doc):
    bag_of_words = dictionary.doc2bow(doc)
    return similarity[lsi[bag_of_words]]

# <codecell>

# A useful function for looking at what's going on.
#
# It takes in a vector of how similar N things are to some input.
# It also takes a 'display_func' to tell it how to show you what
# those N things actually are.
def show_similar(similarities, display_func):
    best_matches = np.argsort(similarities)[::-1][:10]
    for index in best_matches:
        print "%4.4f\t%s" % (similarities[index], display_func(index))

# <codecell>

# And here's the display_func we'll need.
def brief_document(index):
    doc = documents[index]
    return ' '.join(doc)[:200] + '...'

# <codecell>

show_similar(doc_similarities(documents[1]), brief_document)

# <codecell>


