#
# @lc app=leetcode id=1819 lang=python3
#
# [1819] Number of Different Subsequences GCDs
#
# https://leetcode.com/problems/number-of-different-subsequences-gcds/description/
#
# algorithms
# Hard (10.18%)
# Likes:    41
# Dislikes: 18
# Total Accepted:    789
# Total Submissions: 5.6K
# Testcase Example:  '[6,10,3]'
#
# You are given an array nums that consists of positive integers.
# 
# The GCD of a sequence of numbers is defined as the greatest integer that
# divides all the numbers in the sequence evenly.
# 
# 
# For example, the GCD of the sequence [4,6,16] is 2.
# 
# 
# A subsequence of an array is a sequence that can be formed by removing some
# elements (possibly none) of the array.
# 
# 
# For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
# 
# 
# Return the number of different GCDs among all non-empty subsequences of
# nums.
# 
# 
# Example 1:
# 
# 
# Input: nums = [6,10,3]
# Output: 5
# Explanation: The figure shows all the non-empty subsequences and their GCDs.
# The different GCDs are 6, 10, 3, 2, and 1.
# 
# 
# Example 2:
# 
# 
# Input: nums = [5,15,40,5,6]
# Output: 7
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 2 * 10^5
# 
# 
#

# @lc code=start
import math 

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        T = max(nums) + 1
        nums = set(nums)
        ans = 0

        for x in range(1, T):
            g = 0
            for y in range(x, T, x):
                if y in nums:
                    g = gcd(g, y)
                if g == x:
                    break

            if g == x: ans += 1

        return ans
        
# @lc code=end

