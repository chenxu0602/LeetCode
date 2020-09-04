#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (44.97%)
# Likes:    2042
# Dislikes: 125
# Total Accepted:    92.1K
# Total Submissions: 205.1K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#
# Given an array of integers nums and a positive integer k, find whether it's
# possible to divide this array into k non-empty subsets whose sums are all
# equal.
# 
# 
# 
# Example 1:
# 
# 
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3),
# (2,3) with equal sums.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Time  complexity: O(k^(N-k) x k!)
        # Space complexity: O(N)
        target, rem = divmod(sum(nums), k)
        if rem: return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups):
                        return True
                    groups[i] -= v
                if not group: break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return search([0] * k)


        # Time  complexity: O(N x 2^N)
        # Space complexity: O(2^N)
        # target, rem = divmod(sum(nums), k)
        # if rem or max(nums) > target: return False

        # @lru_cache(None)
        # def search(used, todo):
        #     if todo == 0: return True
        #     targ = (todo - 1) % target + 1
        #     return any(search(used | (1 << i), todo - num)
        #                for i, num in enumerate(nums)
        #                if (used >> i) & 1 == 0 and num <= targ)

        # return search(0, target * k)


        
# @lc code=end

