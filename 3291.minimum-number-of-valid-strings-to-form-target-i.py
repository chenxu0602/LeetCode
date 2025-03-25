#
# @lc app=leetcode id=3291 lang=python3
#
# [3291] Minimum Number of Valid Strings to Form Target I
#

# @lc code=start
from collections import defaultdict
from functools import reduce

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:

        Trie = lambda: defaultdict(Trie)
        trie = Trie()

        for word in words:
            reduce(dict.__getitem__, word, trie)['#'] = word

        # trie = {}
        # for word in words:
        #     node = trie
        #     for c in word:
        #         node = node.setdefault(c, {})
        #     node['#'] = word

        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[-1] = 0
        for i in range(n - 1, -1, -1):
            node = trie
            for j in range(i, n):
                if target[j] in node:
                    node = node[target[j]]
                else:
                    break
                dp[i] = min(dp[i], 1 + dp[j + 1])

        return dp[0] if dp[0] < float('inf') else -1

        
# @lc code=end

