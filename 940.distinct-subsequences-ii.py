#
# @lc app=leetcode id=940 lang=python3
#
# [940] Distinct Subsequences II
#
# https://leetcode.com/problems/distinct-subsequences-ii/description/
#
# algorithms
# Hard (41.53%)
# Likes:    387
# Dislikes: 15
# Total Accepted:    11.1K
# Total Submissions: 26.8K
# Testcase Example:  '"abc"'
#
# Given a string S, count the number of distinct, non-empty subsequences of S
# .
# 
# Since the result may be large, return the answer modulo 10^9 + 7.
# 
# 
# 
# Example 1:
# 
# 
# Input: "abc"
# Output: 7
# Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc",
# and "abc".
# 
# 
# 
# Example 2:
# 
# 
# Input: "aba"
# Output: 6
# Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and
# "aba".
# 
# 
# 
# Example 3:
# 
# 
# Input: "aaa"
# Output: 3
# Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
# 
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# S contains only lowercase letters.
# 1 <= S.length <= 2000
# 
# 
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def distinctSubseqII(self, S: str) -> int:
        # Dynamic Programming
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # dp, last = [1], {}
        # for i, x in enumerate(S):
        #     dp.append(dp[-1] * 2)
        #     if x in last:
        #         dp[-1] -= dp[last[x]]
        #     last[x] = i

        # return (dp[-1] - 1) % (10**9 + 7)


        # dp, MOD = [0] * len(S), 10**9 + 7
        # for i, char in enumerate(S):
        #     ind = S.rfind(char, 0, i)
        #     dp[i] = 1 + sum(dp[:i]) % MOD if ind == -1 else sum(dp[ind:i]) % MOD
        # return sum(dp) % MOD


        end = [0] * 26
        for c in S:
            end[ord(c) - ord('a')] = sum(end) + 1
        return sum(end) % (10**9 + 7)
        
# @lc code=end

