#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (41.66%)
# Likes:    1298
# Dislikes: 46
# Total Accepted:    280.2K
# Total Submissions: 657.8K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# Example:
# 
# 
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        """
        if not nums:
            return []

        nums.sort()
        ret = [[]]
        for i in nums:
            new_ret = []
            l = len(ret[-1])
            for seq in ret:
                for j in range(l, -1, -1):
                    if j < l and seq[j] == i:
                        break
                    new_ret.append(seq[:j] + [i] + seq[j:])
            ret = new_ret
        return ret
        """

        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [nums]

        nums, res, prev_num = sorted(nums), [], None

        for i in range(n):
            if nums[i] == prev_num:
                continue
            prev_num = nums[i]
            for j in self.permuteUnique(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + j)

        return res
        
# @lc code=end

