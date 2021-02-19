#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#
# https://leetcode.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (43.55%)
# Likes:    1345
# Dislikes: 75
# Total Accepted:    73.6K
# Total Submissions: 168.8K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# Given an array which consists of non-negative integers and an integer m, you
# can split the array into m non-empty continuous subarrays. Write an algorithm
# to minimize the largest sum among these m subarrays.
# 
# 
# Note:
# If n is the length of array, assume the following constraints are satisfied:
# 
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
# 
# 
# 
# Examples: 
# 
# Input:
# nums = [7,2,5,10,8]
# m = 2
# 
# Output:
# 18
# 
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
# 
# 
#

# @lc code=start
import itertools

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # Dynamic Programming 
        # Let's define f[i][j] to be the minimum largest subarray sum for splitting nums[0...i] into j parts.
        # Consider the jth subarray. We can split the array from a smaller index k to i to form it.
        # Thus f[i][j] can be derived from max(f[k][j-1], nums[k+1] + ... + nums[i]).
        # For all valid index k, f[i][j] should choose the minimum value of the above formula.
        # Time  complexity: O(n^2 x m)
        # Space complexity: O(n x m)
        # n = len(nums)
        # sums = [0] + list(itertools.accumulate(nums))

        # dp = [[float("inf")] * (m + 1) for _ in range(n + 1)]
        # dp[0][0] = 0

        # for i in range(1, n + 1):
        #     for j in range(1, m + 1):
        #         dp[i][j] = min([max(dp[k][j-1], sums[i] - sums[k]) for k in range(i)])

        # return dp[n][m]


        # Binary Search + Greedy
        # Time  complexity: O(nlog(sum(array)))
        # Space complexity: O(n)
        n = len(nums)
        l, r = max(nums), sum(nums)

        ans = r
        while l <= r:
            mid = (l + r) >> 1
            s, cnt = 0, 1
            for i in range(n):
                if s + nums[i] > mid:
                    cnt += 1
                    s = nums[i]
                else:
                    s += nums[i]

            if cnt <= m:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1

        return ans

        

        
# @lc code=end

