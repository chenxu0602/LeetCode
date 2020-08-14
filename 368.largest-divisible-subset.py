#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#
# https://leetcode.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (38.08%)
# Likes:    1414
# Dislikes: 70
# Total Accepted:    96.3K
# Total Submissions: 253.3K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct positive integers, find the largest subset such that
# every pair (Si, Sj) of elements in this subset satisfies:
# 
# Si % Sj = 0 or Sj % Si = 0.
# 
# If there are multiple solutions, return any subset is fine.
# 
# Example 1:
# 
# 
# 
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,4,8]
# Output: [1,2,4,8]
# 
# 
# 
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Corollary I: For any value that can be divided by the largest element in the divisible subset, by adding the new value into the subset, 
        # one can form another divisible subset, i.e. for all h, if h % G == 0, then [E, F, G, h] forms a new divisible subset.
        # Corollary II: For all value that can divide the smallest element in the subset, by adding the new value into the subset, 
        # one can form another divisible subset, i.e. for all d, if E % d == 0, then [d, E, F, G] forms a new divisble subset.


        # Dynamic Programming
        # Time  complexity: O(N^2)
        # Space complexity: O(N^2)
        # The container that holds all intermediate solutions.
        # key: the largest element in a valid subset.
        subsets = {-1: set()}
        for num in sorted(nums):
            subsets[num] = max([subsets[k] for k in subsets if num % k == 0], key=len) | {num}

        return list(max(subsets.values(), key=len))
        

        # Dynamic Programming
        # Time  complexity: O(N^2)
        # Space complexity: O(N)
        # if len(nums) == 0: return [] 
        # nums.sort()
        # # The container that keep the size of the largest divisible subset that ends with X_i
        # # dp[i] corresponds to len(EDS(X_i))
        # dp = [0] * len(nums)
        # """ Build the dynamic programming matrix/vector """
        # for i, num in enumerate(nums):
        #     maxSubsetSize = 0 
        #     for k in range(i):
        #         if nums[i] % nums[k] == 0:
        #             maxSubsetSize = max(maxSubsetSize, dp[k])

        #     maxSubsetSize += 1
        #     dp[i] = maxSubsetSize

        # """ Find both the size of largest divisible set and its index """ 
        # maxSize, maxSizeIndex = max([(v, i) for i, v in enumerate(dp)])
        # ret = []
        # """ Reconstruct the largest divisible subset """ 
        # # currSize: the size of the current subset
        # # currTail: the last element in the current subset
        # currSize, currTail = maxSize, nums[maxSizeIndex]
        # for i in range(maxSizeIndex, -1, -1):
        #     if currSize == dp[i] and currTail % nums[i] == 0:
        #         ret.append(nums[i])
        #         currSize -= 1
        #         currTail = nums[i]

        # return reversed(ret)
# @lc code=end

