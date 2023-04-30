#
# @lc app=leetcode id=2657 lang=python3
#
# [2657] Find the Prefix Common Array of Two Arrays
#

# @lc code=start
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        res = []
        seen = cur = 0
        for ab in zip(A, B):
            for a in ab:
                if (1 << a) & seen:
                    cur += 1
                seen |= 1 << a
            res.append(cur)
        return res

        
# @lc code=end

