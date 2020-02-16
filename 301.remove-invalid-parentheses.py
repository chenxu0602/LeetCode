#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#
# https://leetcode.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (39.37%)
# Likes:    1397
# Dislikes: 60
# Total Accepted:    126.3K
# Total Submissions: 320.6K
# Testcase Example:  '"()())()"'
#
# Remove the minimum number of invalid parentheses in order to make the input
# string valid. Return all possible results.
# 
# Note: The input string may contain letters other than the parentheses ( and
# ).
# 
# Example 1:
# 
# 
# Input: "()())()"
# Output: ["()()()", "(())()"]
# 
# 
# Example 2:
# 
# 
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
# 
# 
# Example 3:
# 
# 
# Input: ")("
# Output: [""]
# 
#
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # level = {s}
        # while True:
        #     valid = []
        #     for s in level:
        #         try:
        #             eval('0,' + filter('()'.count, s).replace(')', '),'))
        #             valid.append(s)
        #         except:
        #             pass

        #     if valid:
        #         return valid

        #     level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

        # def isValid(s):
        #     ctr = 0
        #     for c in s:
        #         if c == '(':
        #             ctr += 1
        #         elif c == ')':
        #             ctr -= 1
        #             if ctr < 0:
        #                 return False

        #     return ctr == 0

        # level = {s}
        # while True:
        #     valid = set(filter(isValid, level))
        #     if valid:
        #         return list(valid)

        #     level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

        def isValid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False

            return ctr == 0

        level = {s}
        while True:
            valid = set(filter(isValid, level))
            if valid:
                return list(valid)
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}
        

