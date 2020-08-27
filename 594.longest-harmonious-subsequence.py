#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#
# https://leetcode.com/problems/longest-harmonious-subsequence/description/
#
# algorithms
# Easy (46.48%)
# Likes:    684
# Dislikes: 85
# Total Accepted:    57.5K
# Total Submissions: 123K
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

# @lc code=start
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # O(n)

        # count = Counter(nums)
        # return max((count[x] + count[x + 1] for x in nums if count[x + 1]), default=0)


        d, res = {}, 0
        for num in nums:
            d[num] = d.setdefault(num, 0) + 1
            if num + 1 in d:
                res = max(res, d[num] + d[num + 1])
            if num - 1 in d:
                res = max(res, d[num] + d[num - 1])
        return res
        
# @lc code=end

