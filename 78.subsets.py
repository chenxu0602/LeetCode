#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (57.78%)
# Likes:    2954
# Dislikes: 70
# Total Accepted:    490.4K
# Total Submissions: 844.1K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # n, output = len(nums), []
        # for i in range(1 << n):
        #     output.append([nums[j] for j in range(n) if i & 1 << j])
        # return output

        res = [[]]
        for num in nums:
            res += [curr + [num] for curr in res]
        return res


        # def backtrack(nums, index, path, res):
        #     res.append(path)
        #     for i in range(index, len(nums)):
        #         backtrack(nums, i + 1, path + [nums[i]], res)

        # res = []
        # backtrack(nums, 0, [], res)
        # return res
        
        
# @lc code=end

