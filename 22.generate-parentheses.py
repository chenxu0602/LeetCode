#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (56.40%)
# Likes:    3431
# Dislikes: 205
# Total Accepted:    405.4K
# Total Submissions: 705K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        if n == 0: return [""]
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-c-1):
                    ans.append("({}){}".format(left, right))
        return ans

        # ans = []
        # def dfs(s="", left=0, right=0):
        #     if len(s) == 2 * n:
        #         ans.append(s)
        #         return
        #     if left < n:
        #         dfs(s+'(', left+1, right)
        #     if right < left:
        #         dfs(s+')', left, right+1)

        # dfs()
        # return ans

        # def generate(p, left, right):
        #     if right >= left >= 0:
        #         if not right:
        #             yield p
        #         for q in generate(p + '(', left - 1, right):
        #             yield q
        #         for q in generate(p + ')', left, right - 1):
        #             yield q
        # return list(generate("", n, n))
                

        # def generteParenthesis2(n, open):
        #     if n > 0 <= open:
        #         return ['(' + p for p in generteParenthesis2(n-1, open+1)] + [')' + p for p in generteParenthesis2(n, open-1)]
        #     return [')' * open] * (not n)
        # return generteParenthesis2(n, 0)
        
# @lc code=end

