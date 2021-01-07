#
# @lc app=leetcode id=1712 lang=python3
#
# [1712] Ways to Split Array Into Three Subarrays
#
# https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/description/
#
# algorithms
# Medium (29.40%)
# Likes:    196
# Dislikes: 29
# Total Accepted:    4.9K
# Total Submissions: 16.8K
# Testcase Example:  '[1,1,1]'
#
# A split of an integer array is good if:
# 
# 
# The array is split into three non-empty contiguous subarrays - named left,
# mid, right respectively from left to right.
# The sum of the elements in left is less than or equal to the sum of the
# elements in mid, and the sum of the elements in mid is less than or equal to
# the sum of the elements in right.
# 
# 
# Given nums, an array of non-negative integers, return the number of good ways
# to split nums. As the number may be too large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1]
# Output: 1
# Explanation: The only good way to split nums is [1] [1] [1].
# 
# Example 2:
# 
# 
# Input: nums = [1,2,2,2,5,0]
# Output: 3
# Explanation: There are three good ways of splitting nums:
# [1] [2] [2,2,5,0]
# [1] [2,2] [2,5,0]
# [1,2] [2,2] [5,0]
# 
# 
# Example 3:
# 
# 
# Input: nums = [3,2,1]
# Output: 0
# Explanation: There is no good way to split nums.
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^4
# 
#

# @lc code=start
import bisect

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        # Binary Search
        # Time  complexity: O(NlogN)
        # Space complexity: O(N)
        n = len(nums)
        MOD = 10**9 + 7
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        def binarySearchLeft(i, target):
            # in nums[i+1:n-1] find the min j s.t.
            # nums[i+1]+...+nums[j] >= target
            left, right = i + 1, n - 2
            while left < right:
                mid = (left + right) // 2
                current = pre_sum[mid + 1] - pre_sum[i + 1]
                if current >= target:
                    right = mid
                else:
                    left = mid + 1
            return left

        def binarySearchRight(i, target):
            # in nums[i+1:n-1] find the max j s.t.
            # nums[i+1]+...+nums[j] <= target
            left, right = i + 1, n - 2
            while left < right:
                mid = (left + right) // 2 + 1
                current = pre_sum[mid + 1] - pre_sum[i + 1]
                if current > target:
                    right = mid - 1
                else:
                    left = mid
            return left

        result = 0
        for i in range(n - 2):
            # nums[0],...,nums[i] | nums[i+1], nums[i+2], ...
            left_sum = pre_sum[i + 1]
            remain = pre_sum[n] - left_sum
            if remain < left_sum * 2:
                break
            # first = bisect.bisect_left(pre_sum, left_sum + left_sum, i + 2, n)
            # last = bisect.bisect_right(pre_sum, left_sum + remain // 2, i + 2, n) - 1
            first = binarySearchLeft(i, left_sum)
            last = binarySearchRight(i, remain // 2)
            result += max(last - first + 1, 0)
            print(left_sum, remain, first, last)

        return result % MOD



        
# @lc code=end

