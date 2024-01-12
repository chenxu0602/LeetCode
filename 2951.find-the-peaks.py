#
# @lc app=leetcode id=2951 lang=python3
#
# [2951] Find the Peaks
#

# @lc code=start
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        return [idx + 1 for idx, (a, b, c) in enumerate(zip(mountain, mountain[1:], mountain[2:])) if a < b > c]
        
# @lc code=end

