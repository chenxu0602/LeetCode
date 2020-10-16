#
# @lc app=leetcode id=1106 lang=python3
#
# [1106] Parsing A Boolean Expression
#
# https://leetcode.com/problems/parsing-a-boolean-expression/description/
#
# algorithms
# Hard (58.49%)
# Likes:    283
# Dislikes: 18
# Total Accepted:    11.2K
# Total Submissions: 19K
# Testcase Example:  '"!(f)"'
#
# Return the result of evaluating a given boolean expression, represented as a
# string.
# 
# An expression can either be:
# 
# 
# "t", evaluating to True;
# "f", evaluating to False;
# "!(expr)", evaluating to the logical NOT of the inner expression expr;
# "&(expr1,expr2,...)", evaluating to the logical AND of 2 or more inner
# expressions expr1, expr2, ...;
# "|(expr1,expr2,...)", evaluating to the logical OR of 2 or more inner
# expressions expr1, expr2, ...
# 
# 
# 
# Example 1:
# 
# 
# Input: expression = "!(f)"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: expression = "|(f,t)"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: expression = "&(t,f)"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: expression = "|(&(t,f,t),!(t))"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= expression.length <= 20000
# expression[i] consists of characters in {'(', ')', '&', '|', '!', 't', 'f',
# ','}.
# expression is a valid expression representing a boolean, as given in the
# description.
# 
# 
#

# @lc code=start
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # S = expression
        # t, f = True, False
        # return eval(S.replace('!', 'not |').replace('&(', 'all([').replace('|(', 'any([').replace(')', '])'))

        if not expression:
            return True

        funcs, exprs = [], []

        functions = {'|': any, '!': lambda x: x[0] ^ True, '&': all}
        bools = {'t': True, 'f': False}

        for c in expression:
            if c in functions:
                exprs.append(list())
                funcs.append(functions.get(c))
            elif c in bools:
                exprs[-1].append(bools.get(c))
            elif c == ')':
                cur = funcs.pop()(exprs.pop())
                if len(exprs):
                    exprs[-1].append(cur)
                else:
                    exprs.append([cur])

        return exprs[-1][0]
        
# @lc code=end

