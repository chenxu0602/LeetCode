#
# @lc app=leetcode id=3014 lang=python3
#
# [3014] Minimum Number of Pushes to Type Word I
#

# @lc code=start
class Solution:
    def minimumPushes(self, word: str) -> int:

        # return sum(i // 8 + 1 for i in range(len(word)))

        n = len(word)
        return (1 + n // 8) * (n // 8) * 4 + (n // 8 + 1) * (n % 8)
        
# @lc code=end

