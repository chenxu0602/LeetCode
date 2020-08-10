#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#
# https://leetcode.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (41.53%)
# Likes:    2044
# Dislikes: 84
# Total Accepted:    171.9K
# Total Submissions: 413.9K
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

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        # O(2^N) / O(N)
        def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    ans = "".join(expr)
                    self.result[ans] = 1
            else:
                # The discard case. Note that here we have our pruning condition.
                # We don't recurse if the remaining count for that parenthesis is == 0.
                if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                    recurse(s, index + 1, left_count, right_count,
                            left_rem - (s[index] == '('), right_rem - (s[index] == ')'), expr)


                expr.append(s[index])

                # Simply recurse one step further if the current character is not a parenthesis.
                if s[index] != '(' and s[index] != ')':
                    recurse(s, index + 1, left_count, right_count,
                            left_rem, right_rem, expr)
                elif s[index] == '(':
                    # Consider an opening bracket.
                    recurse(s, index + 1, left_count + 1, right_count,
                            left_rem, right_rem, expr)
                elif s[index] == ')' and left_count > right_count:
                    # Consider a closing bracket.
                    recurse(s, index + 1, left_count, right_count + 1,
                            left_rem, right_rem, expr)

                # Pop for backtracking.
                expr.pop()

        left, right = 0, 0

        # First, we find out the number of misplaced left and right parentheses.
        for char in s:
            if char == '(':
                left += 1
            elif char == ')':
                # If we don't have a matching left, then this is a misplaced right, record it.
                right = right + 1 if left == 0 else right

                left = left - 1 if left > 0 else left

        self.result = {}
        recurse(s, 0, 0, 0, left, right, [])
        return list(self.result.keys())
                    



        # def isValid(s):
        #     ctr = 0
        #     for c in s:
        #         if c == '(':
        #             ctr += 1
        #         elif c == ')':
        #             ctr -= 1
        #         if ctr < 0:
        #             return False
        #     return ctr == 0

        # level = {s}
        # while True:
        #     valid = set(filter(isValid, level))
        #     if valid:
        #         return list(valid)
        #     level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}
        
# @lc code=end

