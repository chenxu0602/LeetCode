#
# @lc app=leetcode id=2531 lang=python3
#
# [2531] Make Number of Distinct Characters Equal
#

# @lc code=start
from collections import Counter
import string

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:

        def insertAndRemove(mp, toInsert, toRemove):
            mp[toInsert] += 1
            mp[toRemove] -= 1

            if mp[toRemove] == 0:
                del mp[toRemove]

        mp1, mp2 = Counter(word1), Counter(word2)

        for c1 in string.ascii_lowercase:
            for c2 in string.ascii_lowercase:

                if c1 not in mp1 or c2 not in mp2:
                    continue

                insertAndRemove(mp1, c2, c1)
                insertAndRemove(mp2, c1, c2)

                if len(mp1) == len(mp2):
                    return True

                insertAndRemove(mp1, c1, c2)
                insertAndRemove(mp2, c2, c1)

        return False
        
# @lc code=end

