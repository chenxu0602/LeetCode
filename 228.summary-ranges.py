#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#
# https://leetcode.com/problems/summary-ranges/description/
#
# algorithms
# Medium (36.58%)
# Likes:    440
# Dislikes: 436
# Total Accepted:    143.5K
# Total Submissions: 386.4K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# Given a sorted integer array without duplicates, return the summary of its
# ranges.
# 
# Example 1:
# 
# 
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# 
# 
# Example 2:
# 
# 
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
# 
# 
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        x = set([i-1 for i in nums]) - set(nums)
        y = set([i+1 for i in nums]) - set(nums)

        start = sorted({i+1 for i in x})
        end = sorted({i-1 for i in y})

        return ["{}->{}".format(s, e) if s != e else str(s) for s, e in sorted(zip(start, end))]
        
# @lc code=end

