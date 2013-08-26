
In[1]:

```
from __future__ import unicode_literals
```

In[2]:

```
text = '''"Words," you might say, "are things separated by spaces."'''
```

In[3]:

```
text.split(' ')
```




    [u'"Words,"',
     u'you',
     u'might',
     u'say,',
     u'"are',
     u'things',
     u'separated',
     u'by',
     u'spaces."']



In[4]:

```
text2 = '''Okay, words are sequences of letters that don't include punctuation.'''
```

In[5]:

```
import re
re.findall(r'[A-Za-z]+', text2)
```




    [u'Okay',
     u'words',
     u'are',
     u'sequences',
     u'of',
     u'letters',
     u'that',
     u'don',
     u't',
     u'include',
     u'punctuation']



In[6]:

```
text3 = '''Isn't it naïve to not include the apostrophe?'''
```

In[7]:

```
re.findall(r"[A-Za-z']+", text3)
```




    [u"Isn't",
     u'it',
     u'na',
     u've',
     u'to',
     u'not',
     u'include',
     u'the',
     u'apostrophe']



In[8]:

```
text4 = "Fine, let's use NLTK. That shouldn't be too hard."
```

In[9]:

```
import nltk
```

In[10]:

```
[nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(text4)]
```




    [[u'Fine', u',', u'let', u"'s", u'use', u'NLTK', u'.'],
     [u'That', u'should', u"n't", u'be', u'too', u'hard', u'.']]



In[11]:

```
text = 'この文も、言葉で構成されています'
# Translation: "This sentence is also made of words"
```

In[12]:

```
for word in nltk.word_tokenize(text): print(word)
```


    この文も、言葉で構成されています


In[13]:

```
from metanl import japanese
```

In[14]:

```
for word in japanese.normalize_list(text): print(word)
```


    文
    言葉
    構成


In[15]:

```
text2 = 'You might be wondering whether we can deal with suffixes in English'
```

In[16]:

```
from metanl import english
```

In[17]:

```
english.normalize_list(text2)
```




    [u'you',
     u'might',
     u'be',
     u'wonder',
     u'whether',
     u'we',
     u'can',
     u'deal',
     u'with',
     u'suffix',
     u'in',
     u'english']


