#
# @lc app=leetcode id=2178 lang=python3
#
# [2178] Maximum Split of Positive Even Integers
#

# @lc code=start
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        ans, i = [], 2
        if finalSum % 2 == 0:
            while i <= finalSum:
                ans.append(i)
                finalSum -= i
                i += 2
            ans[-1] += finalSum
        return ans
        
# @lc code=end

