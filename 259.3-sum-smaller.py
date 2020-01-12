#
# @lc app=leetcode id=259 lang=python3
#
# [259] 3Sum Smaller
#
# https://leetcode.com/problems/3sum-smaller/description/
#
# algorithms
# Medium (45.40%)
# Likes:    436
# Dislikes: 35
# Total Accepted:    55.8K
# Total Submissions: 121.8K
# Testcase Example:  '[-2,0,1,3]\n2'
#
# Given an array of n integers nums and a target, find the number of index
# triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] +
# nums[j] + nums[k] < target.
# 
# Example:
# 
# 
# Input: nums = [-2,0,1,3], and target = 2
# Output: 2 
# Explanation: Because there are two triplets which sums are less than
# 2:
# [-2,0,1]
# ⁠            [-2,0,3]
# 
# 
# Follow up: Could you solve it in O(n^2) runtime?
# 
#

# @lc code=start
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n, r = len(nums), 0

        for i, num in enumerate(nums):
            j, k, t = i+1, n-1, target - num
            while j < k:
                s = nums[j] + nums[k]
                if s < t:
                    r += k - j
                    j += 1
                else:
                    k -= 1
        return r

        """
        def twoSumSmaller(nums, start, target):
            left, right, s = start, len(nums)-1, 0
            while left < right:
                if nums[left] + nums[right] < target:
                    s += right - left
                    left += 1
                else:
                    right -= 1
            return s


        nums.sort()
        s = 0
        for i in range(len(nums)-2):
            s += twoSumSmaller(nums, i+1, target-nums[i])
        return s
        """

        
# @lc code=end

