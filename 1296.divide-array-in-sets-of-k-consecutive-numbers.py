#
# @lc app=leetcode id=1296 lang=python3
#
# [1296] Divide Array in Sets of K Consecutive Numbers
#
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/description/
#
# algorithms
# Medium (48.09%)
# Likes:    135
# Dislikes: 10
# Total Accepted:    8.8K
# Total Submissions: 18.3K
# Testcase Example:  '[1,2,3,3,4,4,5,6]\n4'
#
# Given an array of integers nums and a positive integer k, find whether it's
# possible to divide this array into sets of k consecutive numbers
# Return True if its possible otherwise return False.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,3,4,4,5,6], k = 4
# Output: true
# Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# Output: true
# Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and
# [9,10,11].
# 
# 
# Example 3:
# 
# 
# Input: nums = [3,3,2,2,1,1], k = 3
# Output: true
# 
# 
# Example 4:
# 
# 
# Input: nums = [1,2,3,4], k = 3
# Output: false
# Explanation: Each array should be divided in subarrays of size 3.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= k <= nums.length
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if not len(nums) % k == 0:
            return False

        count = Counter(nums)
        keys = sorted(count.keys())

        for n in keys:
            if count[n] > 0:
                minus = count[n]
                for i in range(n, n + k):
                    if count[i] < minus:
                        return False
                    count[i] -= minus
        
        return True
        
# @lc code=end

