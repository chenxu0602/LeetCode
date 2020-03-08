#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (54.38%)
# Likes:    2446
# Dislikes: 58
# Total Accepted:    429K
# Total Submissions: 770.8K
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
        
        """
        res = []
        nums.sort()
        for i in range(1 << len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & 1 << j:
                    tmp.append(nums[j])
            res.append(tmp)
        return res
        """

        """
        def dfs(nums, index, path, res):
            res.append(path)
            for i in range(index, len(nums)):
                dfs(nums, i+1, path+[nums[i]], res)

        res = []
        dfs(sorted(nums), 0, [], res)
        return res
        """

        res = [[]]
        for num in nums:
            res += [cur + [num] for cur in res]
        return res

        
# @lc code=end

