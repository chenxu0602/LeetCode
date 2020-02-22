#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (59.92%)
# Likes:    3017
# Dislikes: 92
# Total Accepted:    509.8K
# Total Submissions: 849K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # def dfs(nums, path, res):
        #     if not nums:
        #         res.append(path)
        #     for i in range(len(nums)):
        #         dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

        # res = []
        # dfs(nums, [], res)
        # return res

        if len(nums) == 0: return []
        if len(nums) == 1: return [nums]

        res = []
        for i in range(len(nums)):
            for j in self.permute(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + j)

        return res
        
# @lc code=end

