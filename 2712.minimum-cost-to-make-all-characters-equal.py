#
# @lc app=leetcode id=2712 lang=python3
#
# [2712] Minimum Cost to Make All Characters Equal
#

# @lc code=start
class Solution:
    def minimumCost(self, s: str) -> int:

        ans = 0
        n = len(s)
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                ans += min(i + 1, n - i - 1)
        return ans
        
# @lc code=end

