#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#
# https://leetcode.com/problems/longest-harmonious-subsequence/description/
#
# algorithms
# Easy (44.16%)
# Likes:    436
# Dislikes: 61
# Total Accepted:    39.2K
# Total Submissions: 88.6K
# Testcase Example:  '[1,3,2,2,5,2,3,7]'
#
# We define a harmounious array as an array where the difference between its
# maximum value and its minimum value is exactly 1.
# 
# Now, given an integer array, you need to find the length of its longest
# harmonious subsequence among all its possible subsequences.
# 
# Example 1:
# 
# 
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# 
# 
# 
# 
# Note: The length of the input array will not exceed 20,000.
# 
#
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hashmap, res = {}, 0

        for num in nums:
            hashmap[num] = hashmap.setdefault(num, 0) + 1
            if num + 1 in hashmap:
                res = max(res, hashmap[num] + hashmap[num+1])
            if num - 1 in hashmap:
                res = max(res, hashmap[num] + hashmap[num-1])

        return res

        

