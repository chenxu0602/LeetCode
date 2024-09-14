#
# @lc app=leetcode id=3213 lang=python3
#
# [3213] Construct String with Minimum Cost
#

# @lc code=start
from collections import defaultdict
from functools import reduce

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        END = True

        for word, cost in zip(words, costs):
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            if END not in node or cost < node[END]:
                node[END] = cost

        n = len(target)
        dp = [float('inf')] * n + [0]
        for i in range(n - 1, -1, -1):
            j, node = i, trie
            while j < n and target[j] in node:
                node = node[target[j]]
                if END in node and dp[i] > dp[j + 1] + node[END]:
                    dp[i] = dp[j + 1] + node[END]
                j += 1

        return dp[0] if dp[0] < float('inf') else -1


        
# @lc code=end

