#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (42.92%)
# Likes:    1122
# Dislikes: 51
# Total Accepted:    256.5K
# Total Submissions: 584.6K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note:
# 
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, start, path):
            if target == 0 and path not in res:
                return res.append(path)
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if target < candidates[i]:
                    return
                dfs(candidates, target-candidates[i], i+1, path+[candidates[i]])


        candidates.sort()
        res = []
        dfs(candidates, target, 0, [])
        return res
        
# @lc code=end

