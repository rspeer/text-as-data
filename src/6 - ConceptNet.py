# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import requests
import json

# <codecell>

BASE = 'http://conceptnet5.media.mit.edu/data/5.2'

# <codecell>

def conceptnet_lookup(uri):
    return requests.get(BASE + uri).json()

# <codecell>

for edge in conceptnet_lookup('/c/en/learn')['edges']:
    print [edge['rel'], edge['start'], edge['end']]

# <codecell>

conceptnet_lookup('/assoc/list/en/good@1,bad@-1')

# <codecell>

conceptnet_lookup('/assoc/list/en/good@1,bad@-1?filter=/c/en')

# <codecell>

conceptnet_lookup('/assoc/list/en/good@-1,bad@1?filter=/c/en')

# <codecell>

conceptnet_lookup('/assoc/c/en/travel?filter=/c/en')

