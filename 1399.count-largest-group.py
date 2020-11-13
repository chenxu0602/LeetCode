#
# @lc app=leetcode id=1399 lang=python3
#
# [1399] Count Largest Group
#
# https://leetcode.com/problems/count-largest-group/description/
#
# algorithms
# Easy (65.16%)
# Likes:    136
# Dislikes: 321
# Total Accepted:    17.7K
# Total Submissions: 27.1K
# Testcase Example:  '13\r'
#
# Given an integer n. Each number from 1 to n is grouped according to the sum
# of its digits. 
# 
# Return how many groups have the largest size.
# 
# 
# Example 1:
# 
# 
# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, they are grouped according sum of
# its digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups
# with largest size.
# 
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: 2
# Explanation: There are 2 groups [1], [2] of size 1.
# 
# 
# Example 3:
# 
# 
# Input: n = 15
# Output: 6
# 
# 
# Example 4:
# 
# 
# Input: n = 24
# Output: 5
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def countLargestGroup(self, n: int) -> int:
        d, m = {}, 0
        for i in range(1, n + 1):
            s = sum(map(int, str(i)))
            d[s] = d.get(s, 0) + 1
            m = max(m, d[s])
        return sum(1 for i, v in d.items() if v == m)
        
# @lc code=end

