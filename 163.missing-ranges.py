#
# @lc app=leetcode id=163 lang=python3
#
# [163] Missing Ranges
#
# https://leetcode.com/problems/missing-ranges/description/
#
# algorithms
# Medium (23.42%)
# Likes:    244
# Dislikes: 1449
# Total Accepted:    66.3K
# Total Submissions: 281.1K
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
                res.append("{}->{}".format(s, e))
            elif s == e:
                res.append("{}".format(s))
        return res

        """
        nums = [lower-1] + nums + [upper+1]

        gen = lambda i, j: ["{}->{}".format(i+1, j-1), str(i+1)][i == j-2]

        return [gen(nums[i-1], nums[i]) for i in range(1, len(nums)) if nums[i] - nums[i-1] > 1]
        """
        
# @lc code=end

