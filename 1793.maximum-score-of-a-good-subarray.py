#
# @lc app=leetcode id=1793 lang=python3
#
# [1793] Maximum Score of a Good Subarray
#
# https://leetcode.com/problems/maximum-score-of-a-good-subarray/description/
#
# algorithms
# Hard (46.06%)
# Likes:    220
# Dislikes: 14
# Total Accepted:    5.6K
# Total Submissions: 12.2K
# Testcase Example:  '[1,4,3,7,4,5]\n3'
#
# You are given an array of integers nums (0-indexed) and an integer k.
# 
# The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ...,
# nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.
# 
# Return the maximum possible score of a good subarray.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,4,3,7,4,5], k = 3
# Output: 15
# Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) *
# (5-1+1) = 3 * 5 = 15. 
# 
# 
# Example 2:
# 
# 
# Input: nums = [5,5,4,5,4,1,1,1], k = 0
# Output: 20
# Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) *
# (4-0+1) = 4 * 5 = 20.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 2 * 10^4
# 0 <= k < nums.length
# 
# 
#

# @lc code=start
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        res = mini = nums[k]
        i, j, n = k, k, len(nums)

        while i > 0 or j < n - 1:
            if (nums[i - 1] if i else 0) < (nums[j + 1] if j < n - 1 else 0):
                j += 1
            else:
                i -= 1
            mini = min(mini, nums[i], nums[j])
            res = max(res, mini * (j - i + 1))

        return res

        
# @lc code=end

