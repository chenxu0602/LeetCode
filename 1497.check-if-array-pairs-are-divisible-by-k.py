#
# @lc app=leetcode id=1497 lang=python3
#
# [1497] Check If Array Pairs Are Divisible by k
#
# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/
#
# algorithms
# Medium (40.33%)
# Likes:    326
# Dislikes: 34
# Total Accepted:    15.4K
# Total Submissions: 38.2K
# Testcase Example:  '[1,2,3,4,5,10,6,7,8,9]\n5'
#
# Given an array of integers arr of even length n and an integer k.
# 
# We want to divide the array into exactly n / 2 pairs such that the sum of
# each pair is divisible by k.
# 
# Return True If you can find a way to do that or False otherwise.
# 
# 
# Example 1:
# 
# 
# Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# Output: true
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,2,3,4,5,6], k = 7
# Output: true
# Explanation: Pairs are (1,6),(2,5) and(3,4).
# 
# 
# Example 3:
# 
# 
# Input: arr = [1,2,3,4,5,6], k = 10
# Output: false
# Explanation: You can try all possible pairs to see that there is no way to
# divide arr into 3 pairs each with sum divisible by 10.
# 
# 
# Example 4:
# 
# 
# Input: arr = [-10,10], k = 2
# Output: true
# 
# 
# Example 5:
# 
# 
# Input: arr = [-1,1,-2,2,-3,3,-4,4], k = 3
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# arr.length == n
# 1 <= n <= 10^5
# n is even.
# -10^9 <= arr[i] <= 10^9
# 1 <= k <= 10^5
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if len(arr) % 2 == 1:
            return False

        cache = defaultdict(int)
        count = 0

        for i, num in enumerate(arr):
            key = k - (num % k)
            if cache[key] >= 1:
                count += 1
                cache[key] -= 1
            else:
                cache[(num % k) or k] += 1

        return count == len(arr) // 2
        
# @lc code=end

