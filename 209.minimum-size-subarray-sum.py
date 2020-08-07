#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (36.56%)
# Likes:    1695
# Dislikes: 93
# Total Accepted:    225.7K
# Total Submissions: 616.5K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
# 
# Example: 
# 
# 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem
# constraint.
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n). 
# 
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        # Time  complexity: O(n)
        # Space complexity: O(1)

        ans, left, ss = float("inf"), 0, 0

        for i in range(len(nums)):
            ss += nums[i]
            while ss >= s:
                ans = min(ans, i - left + 1)
                ss -= nums[left]
                left += 1

        return ans if ans < float("inf") else 0

        
# @lc code=end

