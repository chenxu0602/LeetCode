#
# @lc app=leetcode id=1681 lang=python3
#
# [1681] Minimum Incompatibility
#
# https://leetcode.com/problems/minimum-incompatibility/description/
#
# algorithms
# Hard (32.66%)
# Likes:    77
# Dislikes: 72
# Total Accepted:    3K
# Total Submissions: 9.2K
# Testcase Example:  '[1,2,1,4]\n2'
#
# You are given an integer array nums​​​ and an integer k. You are asked to
# distribute this array into k subsets of equal size such that there are no two
# equal elements in the same subset.
# 
# A subset's incompatibility is the difference between the maximum and minimum
# elements in that array.
# 
# Return the minimum possible sum of incompatibilities of the k subsets after
# distributing the array optimally, or return -1 if it is not possible.
# 
# A subset is a group integers that appear in the array with no particular
# order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,1,4], k = 2
# Output: 4
# Explanation: The optimal distribution of subsets is [1,2] and [1,4].
# The incompatibility is (2-1) + (4-1) = 4.
# Note that [1,1] and [2,4] would result in a smaller sum, but the first subset
# contains 2 equal elements.
# 
# Example 2:
# 
# 
# Input: nums = [6,3,8,1,3,1,2,2], k = 4
# Output: 6
# Explanation: The optimal distribution of subsets is [1,2], [2,3], [6,8], and
# [1,3].
# The incompatibility is (2-1) + (3-2) + (8-6) + (3-1) = 6.
# 
# 
# Example 3:
# 
# 
# Input: nums = [5,3,3,6,3,3], k = 3
# Output: -1
# Explanation: It is impossible to distribute nums into 3 subsets where no two
# elements are equal in the same subset.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= nums.length <= 16
# nums.length is divisible by k
# 1 <= nums[i] <= nums.length
# 
# 
#

# @lc code=start
import itertools

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        # 'l' means last added
        # O(n x 2^n)
        n = len(nums)
        if k == n: return 0
        nums.sort()
        dp = [[float("inf")] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = 0

        for mask in range(1 << n):
            n_z_bits = [j for j in range(n) if mask & (1 << j)]
            if len(n_z_bits) % (n // k) == 1:
                for j, l in itertools.permutations(n_z_bits, 2):
                    dp[mask][l] = min(dp[mask][l], dp[mask ^ (1 << l)][j])
            else:
                for j, l in itertools.combinations(n_z_bits, 2):
                    if nums[j] != nums[l]:
                        dp[mask][j] = min(dp[mask][j], dp[mask ^ (1 << j)][l] + nums[l] - nums[j])

        return min(dp[-1]) if min(dp[-1]) != float("inf") else -1



        

        
# @lc code=end

