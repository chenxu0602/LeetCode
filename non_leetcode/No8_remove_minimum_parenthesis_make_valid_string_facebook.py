#!/usr/bin/python
# coding=utf-8
################################################################################
'''
https://leetcode.com/discuss/interview-question/124551/

Given a string str consisting of parentheses (, ) and alphanumeric characters.
Remove minimum number of paranthesis to make the string valid and return any
valid result. In a valid string for every opening/closing parentheses there is
a matching closing/opening one.

Example 1:

Input: "ab(a(c)fg)9)"
Output: "ab(a(c)fg)9" or "ab(a(c)fg9)" or "ab(a(cfg)9)"
Example 2:

Input: ")a(b)c()("
Output: "a(b)c()"
Example 3:

Input: ")("
Output: ""
Example 4:

Input: "a(b))"
Output: "a(b)"
Example 5:

Input: "(a(c()b)"
Output: "a(c()b)" or "(ac()b)" or "(a(c)b)"
Example 6:

Input: "(a)b(c)d(e)f)(g)"
Output: "(a)b(c)d(e)f(g)"
Related problems:

https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
https://leetcode.com/problems/remove-invalid-parentheses is a different problem,
 becuase in this case we need to return only 1 result
'''
################################################################################
'''
hard version Leetcode No301
'''
class Solution(object):

    def remove_invalid_parentheses(self, s):

        N = len(s)
        flag = [False] * N

        left, right = 0, 0
        for i in range(N):
            if s[i] == '(':
                left += 1
            elif s[i] == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
                    flag[i] = True

        left, right = 0, 0
        for i in range(N - 1, -1, -1):
            if s[i] == ')':
                right += 1
            elif s[i] == '(':
                if right > 0:
                    right -= 1
                else:
                    flag[i] = True
                    left += 1

        return ''.join([s[i] for i in range(N) if flag[i] is False])

    #similar to this!
    #calcualte how many ( and ) are not legal in string s
    def count_left_right(self, s):
        left, right = 0, 0
        for char in s:
            if char == '(':
                left += 1
            elif char == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left, right

a = Solution()
print a.remove_invalid_parentheses("ab(a(c)fg)9)")
print a.remove_invalid_parentheses(")a(b)c()(")
print a.remove_invalid_parentheses(')(')
print a.remove_invalid_parentheses("a(b))")
print a.remove_invalid_parentheses("(a(c()b)")
print a.remove_invalid_parentheses("(a)b(c)d(e)f)(g)")
