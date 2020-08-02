#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#
# https://leetcode.com/problems/candy/description/
#
# algorithms
# Hard (31.48%)
# Likes:    978
# Dislikes: 165
# Total Accepted:    132.5K
# Total Submissions: 420K
# Testcase Example:  '[1,0,2]'
#
# There are N children standing in a line. Each child is assigned a rating
# value.
# 
# You are giving candies to these children subjected to the following
# requirements:
# 
# 
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# 
# 
# What is the minimum candies you must give?
# 
# Example 1:
# 
# 
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1,
# 2 candies respectively.
# 
# 
# Example 2:
# 
# 
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2,
# 1 candies respectively.
# ⁠            The third child gets 1 candy because it satisfies the above two
# conditions.
# 
# 
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:

        res = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1

        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i-1] > ratings[i]:
                res[i-1] = max(res[i-1], res[i] + 1)

        return sum(res)
        
# @lc code=end

