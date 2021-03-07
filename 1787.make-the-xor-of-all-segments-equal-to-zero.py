#
# @lc app=leetcode id=1787 lang=python3
#
# [1787] Make the XOR of All Segments Equal to Zero
#
# https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/description/
#
# algorithms
# Hard (22.20%)
# Likes:    34
# Dislikes: 4
# Total Accepted:    598
# Total Submissions: 2.3K
# Testcase Example:  '[1,2,0,3,0]\n1'
#
# You are given an array nums​​​ and an integer k​​​​​. The XOR of a segment
# [left, right] where left <= right is the XOR of all the elements with indices
# between left and right, inclusive: nums[left] XOR nums[left+1] XOR ... XOR
# nums[right].
# 
# Return the minimum number of elements to change in the array such that the
# XOR of all segments of size k​​​​​​ is equal to zero.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,0,3,0], k = 1
# Output: 3
# Explanation: Modify the array from [1,2,0,3,0] to from [0,0,0,0,0].
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,4,5,2,1,7,3,4,7], k = 3
# Output: 3
# Explanation: Modify the array from [3,4,5,2,1,7,3,4,7] to
# [3,4,7,3,4,7,3,4,7].
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,4,1,2,5,1,2,6], k = 3
# Output: 3
# Explanation: Modify the array from [1,2,4,1,2,5,1,2,6] to
# [1,2,3,1,2,3,1,2,3].
# 
# 
# Constraints:
# 
# 
# 1 <= k <= nums.length <= 2000
# ​​​​​​0 <= nums[i] < 2^10
# 
# 
#

# @lc code=start
from collections import defaultdict, Counter
from functools import lru_cache

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnts = [Counter(nums[j] for j in range(i, n, k)) for i in range(k)]

        # case 1: one number is not from list
        mxs = [cnts[i].most_common(1)[0][1] for i in range(k)]
        ans = n - (sum(mxs) - min(mxs))

        # case 2: all k numbers are from list
        d = cnts[0]
        for i in range(1, k):
            d2 = defaultdict(int)
            for x in d:
                for y in cnts[i]:
                    t = x ^ y
                    d2[t] = max(d2[t], d[x] + cnts[i][y])

            d = d2

        return min(ans, n - d[0])


        # n = 1 << 10

        # freq = defaultdict(Counter)
        # for i, num in enumerate(nums):
        #     freq[i % k][num] += 1

        # dp = [[0] * n for _ in range(k + 1)]
        # for i in range(1, n):
        #     dp[0][i] = -float("inf")

        # for i in range(1, k + 1):
        #     max_row = max(dp[i - 1])

        #     for j in range(n):
        #         for mask in freq[i - 1]:
        #             dp[i][j] = max(dp[i][j], max_row, dp[i - 1][j ^ mask] + freq[i - 1][mask])

        # return len(nums) - dp[-1][0]

        
        
# @lc code=end

