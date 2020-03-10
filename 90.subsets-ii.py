#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (45.19%)
# Likes:    1331
# Dislikes: 58
# Total Accepted:    249.4K
# Total Submissions: 551.5K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
# 
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # def dfs(depth, start, L):
        #     if L not in res:
        #         res.append(L)
        #     if depth == len(nums):
        #         return
        #     for i in range(start, len(nums)):
        #         dfs(depth + 1, i + 1, L + [nums[i]])

        # nums.sort()
        # res = []
        # dfs(0, 0, [])
        # return res

        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])

        return res


        
# @lc code=end

