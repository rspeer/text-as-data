# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import nltk
from nltk.corpus import movie_reviews
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
import numpy as np
import random

# <codecell>

# Get a list of (document text, category)
documents = [
    (movie_reviews.raw(fileid), category)
    for category in movie_reviews.categories()
    for fileid in movie_reviews.fileids(category)
]
random.seed(3)
random.shuffle(documents)

# <codecell>

reviewtext, rating = documents[0]
print reviewtext
print rating

# <codecell>

train_samples, test_samples = documents[:1000], documents[1000:]

# <codecell>

# Make feature vectors out of the documents, based on which words they contain
vectorizer = CountVectorizer(binary=True)
train_vectors = vectorizer.fit_transform([doc for doc, target in train_samples])
test_vectors = vectorizer.transform([doc for doc, target in test_samples])
train_targets = [target for doc, target in train_samples]
test_targets = [target for doc, target in test_samples]

# <codecell>

classifier = BernoulliNB()

# <codecell>

classifier.fit(train_vectors, train_targets)

# <codecell>

classifier.score(test_vectors, test_targets)

# <codecell>

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
    

# <codecell>

show_most_informative_features(vectorizer, classifier)

# <codecell>


