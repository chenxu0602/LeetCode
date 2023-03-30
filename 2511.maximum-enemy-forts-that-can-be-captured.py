#
# @lc app=leetcode id=2511 lang=python3
#
# [2511] Maximum Enemy Forts That Can Be Captured
#

# @lc code=start
class Solution:
    def captureForts(self, forts: List[int]) -> int:

        # this problem can be translated into "finding the number of 0's between a 1 and a -1".
        ans = ii = 0
        for i, v in enumerate(forts):
            if v:
                if forts[ii] == -v:
                    ans = max(ans, i - ii - 1)
                ii = i
        return ans

        
# @lc code=end

