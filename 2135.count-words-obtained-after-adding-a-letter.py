#
# @lc app=leetcode id=2135 lang=python3
#
# [2135] Count Words Obtained After Adding a Letter
#

# @lc code=start
from tracemalloc import start


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:

        seen = set()
        for word in startWords:
            m = 0
            for ch in word:
                m ^= 1 << ord(ch) - 97
            seen.add(m)

        ans = 0
        for word in targetWords:
            m = 0
            for ch in word:
                m ^= 1 << ord(ch) - 97
            for ch in word:
                if m ^ (1 << ord(ch) - 97) in seen:
                    ans += 1
                    break

        return ans
        
        
# @lc code=end

