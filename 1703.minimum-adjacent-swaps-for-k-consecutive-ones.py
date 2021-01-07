#
# @lc app=leetcode id=1703 lang=python3
#
# [1703] Minimum Adjacent Swaps for K Consecutive Ones
#
# https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/description/
#
# algorithms
# Hard (40.71%)
# Likes:    121
# Dislikes: 4
# Total Accepted:    2K
# Total Submissions: 4.9K
# Testcase Example:  '[1,0,0,1,0,1]\n2'
#
# You are given an integer array, nums, and an integer k. nums comprises of
# only 0's and 1's. In one move, you can choose two adjacent indices and swap
# their values.
# 
# Return the minimum number of moves required so that nums has k consecutive
# 1's.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,0,0,1,0,1], k = 2
# Output: 1
# Explanation: In 1 move, nums could be [1,0,0,0,1,1] and have 2 consecutive
# 1's.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,0,0,0,0,1,1], k = 3
# Output: 5
# Explanation: In 5 moves, the leftmost 1 can be shifted right until nums =
# [0,0,0,0,0,1,1,1].
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,1,0,1], k = 2
# Output: 0
# Explanation: nums already has 2 consecutive 1's.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# nums[i] is 0 or 1.
# 1 <= k <= sum(nums)
# 
# 
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        # Find all index of nums[i] if nums[i] == 1.
        # Now the problem changes to, find k consecute element in A,
        # that has minimum distance to their median sequence.
        # To solve this, we need to use the prefix sum of A, which is B in this solution.
        # Time  complexity: O(n)
        # Space complexity: O(n)
        A = [i for i, a in enumerate(nums) if a]
        n = len(A)
        B = [0] * (n + 1)
        res = float("inf")
        for i in range(n):
            B[i + 1] = B[i] + A[i]

        for i in range(len(A) - k + 1):
            res = min(res, B[i + k] - B[k // 2 + i] - B[(k + 1) // 2 + i] + B[i])
        res -= (k // 2) * ((k + 1) // 2)

        return res
        
# @lc code=end

