#
# @lc app=leetcode id=2766 lang=python3
#
# [2766] Relocate Marbles
#

# @lc code=start
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:

        s = set(nums)
        for f, t in zip(moveFrom, moveTo):
            s.remove(f)
            s.add(t)
        return sorted(s)
        
# @lc code=end

