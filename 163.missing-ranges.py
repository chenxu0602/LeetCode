#
# @lc app=leetcode id=163 lang=python3
#
# [163] Missing Ranges
#
# https://leetcode.com/problems/missing-ranges/description/
#
# algorithms
# Medium (23.82%)
# Likes:    281
# Dislikes: 1657
# Total Accepted:    74.7K
# Total Submissions: 313.1K
# Testcase Example:  '[0,1,3,50,75]\n0\n99'
#
# Given a sorted integer array nums, where the range of elements are in the
# inclusive range [lower, upper], return its missing ranges.
# 
# Example:
# 
# 
# Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# Output: ["2", "4->49", "51->74", "76->99"]
# 
# 
#

# @lc code=start
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        start = [lower] + sorted(set(map(lambda x: x+1, nums)) - set(nums)) 
        end = sorted(set(map(lambda x: x-1, nums)) - set(nums)) + [upper]

        res = []
        for s, e in zip(start, end):
            if s < e:
                res.append(f"{s}->{e}")
            elif s == e:
                res.append(f"{s}")
        return res
        
# @lc code=end

