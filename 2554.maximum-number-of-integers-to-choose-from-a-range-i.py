#
# @lc app=leetcode id=2554 lang=python3
#
# [2554] Maximum Number of Integers to Choose From a Range I
#

# @lc code=start
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        ans, banned = -1, set(banned)

        for i in range(1, n + 1):
            if i not in banned:
                maxSum -= i
                ans += 1

            if maxSum < 0: return ans

        return ans + 1
        
# @lc code=end

