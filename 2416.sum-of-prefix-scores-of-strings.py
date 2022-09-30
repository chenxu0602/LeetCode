#
# @lc app=leetcode id=2416 lang=python3
#
# [2416] Sum of Prefix Scores of Strings
#

# @lc code=start
from collections import Counter

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        counter = Counter()
        for word in words:
            for i in range(len(word)):
                counter[word[:i + 1]] += 1

        ans = []
        for word in words:
            curr = 0
            for i in range(len(word)):
                curr += counter[word[:i + 1]]
            ans.append(curr)

        return ans
        
# @lc code=end

