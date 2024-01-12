#
# @lc app=leetcode id=2957 lang=python3
#
# [2957] Remove Adjacent Almost-Equal Characters
#

# @lc code=start
from itertools import pairwise

class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:

        # res = 0
        # skip = False
        # for i in range(1, len(word)):
        #     diff = ord(word[i]) - ord(word[i - 1])
        #     if not skip and -1 <= diff <= 1:
        #         res += 1
        #         skip = True
        #     else:
        #         skip = False

        # return res


        word = map(ord, word)
        adj_eq, ans = False, 0

        for a, b in pairwise(word):
            if adj_eq or abs(a - b) > 1:
                adj_eq = False
                continue

            adj_eq = True
            ans += 1

        return ans
        
# @lc code=end

