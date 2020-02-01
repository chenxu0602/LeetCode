
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



820:

        words = list(set(words))
        Trie = lambda: defaultdict(Trie)
        trie = Trie()

        nodes = [functools.reduce(dict.__getitem__, word[::-1], trie) for word in words]

        return sum(len(word) + 1 
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)
