#
# @lc app=leetcode id=726 lang=python3
#
# [726] Number of Atoms
#
# https://leetcode.com/problems/number-of-atoms/description/
#
# algorithms
# Hard (46.96%)
# Likes:    315
# Dislikes: 100
# Total Accepted:    16K
# Total Submissions: 34K
# Testcase Example:  '"H2O"'
#
# Given a chemical formula (given as a string), return the count of each atom.
# 
# An atomic element always starts with an uppercase character, then zero or
# more lowercase letters, representing the name.
# 
# 1 or more digits representing the count of that element may follow if the
# count is greater than 1.  If the count is 1, no digits will follow.  For
# example, H2O and H2O2 are possible, but H1O2 is impossible.
# 
# Two formulas concatenated together produce another formula.  For example,
# H2O2He3Mg4 is also a formula.  
# 
# A formula placed in parentheses, and a count (optionally added) is also a
# formula.  For example, (H2O2) and (H2O2)3 are formulas.
# 
# Given a formula, output the count of all elements as a string in the
# following form: the first name (in sorted order), followed by its count (if
# that count is more than 1), followed by the second name (in sorted order),
# followed by its count (if that count is more than 1), and so on.
# 
# Example 1:
# 
# Input: 
# formula = "H2O"
# Output: "H2O"
# Explanation: 
# The count of elements are {'H': 2, 'O': 1}.
# 
# 
# 
# Example 2:
# 
# Input: 
# formula = "Mg(OH)2"
# Output: "H2MgO2"
# Explanation: 
# The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
# 
# 
# 
# Example 3:
# 
# Input: 
# formula = "K4(ON(SO3)2)2"
# Output: "K4N2O14S4"
# Explanation: 
# The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
# 
# 
# 
# Note:
# All atom names consist of lowercase letters, except for the first character
# which is uppercase.
# The length of formula will be in the range [1, 1000].
# formula will only consist of letters, digits, and round parentheses, and is a
# valid formula as defined in the problem.
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        dic, coeff, stack, elem, cnt, i = defaultdict(int), 1, [], '', 0, 0
        for c in formula[::-1]:
            if c.isdigit():
                cnt += int(c) * (10 ** i)
                i += 1
            elif c == ')':
                stack.append(cnt)
                coeff *= cnt
                i = cnt = 0
            elif c == '(':
                coeff //= stack.pop()
                i = cnt = 0
            elif c.isupper():
                elem += c
                dic[elem[::-1]] += (cnt or 1) * coeff
                elem = ''
                i = cnt = 0
            elif c.islower():
                elem += c

        return ''.join(k + str(v > 1 and v or '') for k, v in sorted(dic.items()))

        
# @lc code=end

