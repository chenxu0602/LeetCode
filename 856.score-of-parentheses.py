#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#
# https://leetcode.com/problems/score-of-parentheses/description/
#
# algorithms
# Medium (60.30%)
# Likes:    1274
# Dislikes: 41
# Total Accepted:    40.8K
# Total Submissions: 67.1K
# Testcase Example:  '"()"'
#
# Given a balanced parentheses string S, compute the score of the string based
# on the following rule:
# 
# 
# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "()"
# Output: 1
# 
# 
# 
# Example 2:
# 
# 
# Input: "(())"
# Output: 2
# 
# 
# 
# Example 3:
# 
# 
# Input: "()()"
# Output: 2
# 
# 
# 
# Example 4:
# 
# 
# Input: "(()(()))"
# Output: 6
# 
# 
# 
# 
# Note:
# 
# 
# S is a balanced parentheses string, containing only ( and ).
# 2 <= S.length <= 50
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        # Divide and Conquer
        # Time  complexity: O(N^2)
        # Space complexity: O(N)
        # def F(i, j):
        #     # Score of balanced string S[i:j]
        #     ans = bal = 0
        #     # Split string into primitives
        #     for k in range(i, j):
        #         bal += 1 if S[k] == '(' else -1
        #         if bal == 0:
        #             if k - i == 1:
        #                 ans += 1
        #             else:
        #                 ans += 2 * F(i + 1, k)
        #             i = k + 1

        #     return ans

        # return F(0, len(S))


        # Stack
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # stack = [0]

        # for x in S:
        #     if x == '(':
        #         stack.append(0)
        #     else:
        #         v = stack.pop()
        #         stack[-1] += max(2 * v, 1)

        # return stack.pop()


        # Count Cores
        # Time  complexity: O(N)
        # Space complexity: O(1)
        ans = bal = 0
        for i, x in enumerate(S):
            if x == '(':
                bal += 1
            else:
                bal -= 1
                if S[i - 1] == '(':
                    ans += 1 << bal

        return ans
        
# @lc code=end

