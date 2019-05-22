#W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.

import collections

list2 = []
hhj = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

hhj = hhj.lower()
hhj = hhj.replace(",", " ")
hhj = hhj.split()

print(collections.Counter(hhj))

words = {}

for i in hhj:
    if i in words:
        words[i] += 1
    else:
        words[i] = 1

for k, v in words.items():
    print(k, "\t", v)