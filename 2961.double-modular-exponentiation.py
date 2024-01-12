#
# @lc app=leetcode id=2961 lang=python3
#
# [2961] Double Modular Exponentiation
#

# @lc code=start
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:

        return [i for i, (a, b, c, m) in enumerate(variables) if pow(pow(a, b, 10), c, m) == target]
        
# @lc code=end

