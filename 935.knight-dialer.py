#
# @lc app=leetcode id=935 lang=python3
#
# [935] Knight Dialer
#
# https://leetcode.com/problems/knight-dialer/description/
#
# algorithms
# Medium (43.11%)
# Likes:    388
# Dislikes: 151
# Total Accepted:    24.1K
# Total Submissions: 55.8K
# Testcase Example:  '1'
#
# A chess knight can move as indicated in the chess diagram below:
# 
# .           
# 
# 
# 
# This time, we place our chess knight on any numbered key of a phone pad
# (indicated above), and the knight makes N-1 hops.  Each hop must be from one
# key to another numbered key.
# 
# Each time it lands on a key (including the initial placement of the knight),
# it presses the number of that key, pressing N digits total.
# 
# How many distinct numbers can you dial in this manner?
# 
# Since the answer may be large, output the answer modulo 10^9 + 7.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: 10
# 
# 
# 
# Example 2:
# 
# 
# Input: 2
# Output: 20
# 
# 
# 
# Example 3:
# 
# 
# Input: 3
# Output: 46
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 5000
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def knightDialer(self, N: int) -> int:
        # Dynamic Programming
        # Time  complexity: O(N)
        # Space complexity: O(1)
        MOD = 10**9 + 7
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]

        dp = [1] * 10
        for hops in range(N - 1):
            dp2 = [0] * 10
            for node, count in enumerate(dp):
                for nei in moves[node]:
                    dp2[nei] += count
                    dp2[nei] %= MOD
            dp = dp2

        return sum(dp) % MOD
        
# @lc code=end

