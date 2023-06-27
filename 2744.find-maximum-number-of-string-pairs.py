#
# @lc app=leetcode id=2744 lang=python3
#
# [2744] Find Maximum Number of String Pairs
#

# @lc code=start
from collections import defaultdict

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:

        d = defaultdict(int)

        for word in words:
            d[min(word, word[::-1])] += 1

        return sum(map(lambda x: x * (x - 1), d.values())) // 2
        
# @lc code=end

