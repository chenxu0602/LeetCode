
from collections import defaultdict
from functools import reduce

Trie = lambda: defaultdict(Trie)
trie = Trie()
END = True

for word in words:
    reduce(dict.__getitem__, word, trie)[END] = word

def replace(word):
    cur = trie
    for letter in word:
        if letter not in cur or END in cur:
            break
        cur = cur[letter]
    return cur.get(END, word)
