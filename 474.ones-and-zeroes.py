#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#
# https://leetcode.com/problems/ones-and-zeroes/description/
#
# algorithms
# Medium (42.69%)
# Likes:    1067
# Dislikes: 237
# Total Accepted:    50.2K
# Total Submissions: 117.1K
# Testcase Example:  '["10","0001","111001","1","0"]\n5\n3'
#
# Given an array, strs, with strings consisting of only 0s and 1s. Also two
# integers m and n.
# 
# Now your task is to find the maximum number of strings that you can form with
# given m 0s and n 1s. Each 0 and 1 can be used at most once.
# 
# 
# Example 1:
# 
# 
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: This are totally 4 strings can be formed by the using of 5 0s
# and 3 1s, which are "10","0001","1","0".
# 
# 
# Example 2:
# 
# 
# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: You could form "10", but then you'd have nothing left. Better
# form "0" and "1".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i] consists only of digits '0' and '1'.
# 1 <= m, n <= 100
# 
# 
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Time  complexity: O(l x m x n). Three nested loops are their, where ll is the length of strsstrs, mm and nn are the number of zeroes and ones respectively.
        # Space complexity: O(m x n)
        def countzerosones(s):
            c = [0, 0]
            for i, v in enumerate(s):
                c[ord(v) - ord('0')] += 1
            return c

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            count = countzerosones(s)
            for zeros in range(m, count[0] - 1, -1):
                for ones in range(n, count[1] - 1, -1):
                    dp[zeros][ones] = max(1 + dp[zeros - count[0]][ones - count[1]], dp[zeros][ones])

        return dp[m][n]
        
# @lc code=end

