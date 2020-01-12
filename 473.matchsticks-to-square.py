#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#
# https://leetcode.com/problems/matchsticks-to-square/description/
#
# algorithms
# Medium (36.02%)
# Likes:    334
# Dislikes: 41
# Total Accepted:    25.4K
# Total Submissions: 70.4K
# Testcase Example:  '[1,1,2,2,2]'
#
# Remember the story of Little Match Girl? By now, you know exactly what
# matchsticks the little match girl has, please find out a way you can make one
# square by using up all those matchsticks. You should not break any stick, but
# you can link them up, and each matchstick must be used exactly one time.
# 
# ⁠Your input will be several matchsticks the girl has, represented with their
# stick length. Your output will either be true or false, to represent whether
# you could make one square using all the matchsticks the little match girl
# has.
# 
# Example 1:
# 
# Input: [1,1,2,2,2]
# Output: true
# 
# Explanation: You can form a square with length 2, one side of the square came
# two sticks with length 1.
# 
# 
# 
# Example 2:
# 
# Input: [3,3,3,3,4]
# Output: false
# 
# Explanation: You cannot find a way to form a square with all the
# matchsticks.
# 
# 
# 
# Note:
# 
# The length sum of the given matchsticks is in the range of 0 to 10^9.
# The length of the given matchstick array will not exceed 15.
# 
# 
#
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        
        if not nums:
            return False

        L = len(nums)

        perimeter = sum(nums)

        possible_side = perimeter // 4

        if possible_side * 4 != perimeter:
            return False


        nums.sort(reverse=True)

        sums = [0 for _ in range(4)]

        def dfs(index):
            if index == L:
                return sums[0] == sums[1] == sums[2] == possible_side

            for i in range(4):
                if sums[i] + nums[index] <= possible_side:
                    sums[i] += nums[index]
                    if dfs(index + 1):
                        return True
                    sums[i] -= nums[index]
            return False

        return dfs(0)

