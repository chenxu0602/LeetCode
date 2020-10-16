#
# @lc app=leetcode id=1096 lang=python3
#
# [1096] Brace Expansion II
#
# https://leetcode.com/problems/brace-expansion-ii/description/
#
# algorithms
# Hard (62.18%)
# Likes:    230
# Dislikes: 143
# Total Accepted:    11.9K
# Total Submissions: 19.2K
# Testcase Example:  '"{a,b}{c,{d,e}}"\r'
#
# Under a grammar given below, strings can represent a set of lowercase words.
# Let's use R(expr) to denote the set of words the expression represents.
# 
# Grammar can best be understood through simple examples:
# 
# 
# Single letters represent a singleton set containing that word.
# 
# R("a") = {"a"}
# R("w") = {"w"}
# 
# 
# When we take a comma delimited list of 2 or more expressions, we take the
# union of possibilities.
# 
# R("{a,b,c}") = {"a","b","c"}
# R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each
# word at most once)
# 
# 
# When we concatenate two expressions, we take the set of possible
# concatenations between two words where the first word comes from the first
# expression and the second word comes from the second expression.
# 
# R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
# R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg",
# "acdfh", "acefg", "acefh"}
# 
# 
# 
# 
# Formally, the 3 rules for our grammar:
# 
# 
# For every lowercase letter x, we have R(x) = {x}
# For expressions e_1, e_2, ... , e_k with k >= 2, we have R({e_1,e_2,...}) =
# R(e_1) ∪ R(e_2) ∪ ...
# For expressions e_1 and e_2, we have R(e_1 + e_2) = {a + b for (a, b) in
# R(e_1) × R(e_2)}, where + denotes concatenation, and × denotes the cartesian
# product.
# 
# 
# Given an expression representing a set of words under the given grammar,
# return the sorted list of words that the expression represents.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "{a,b}{c,{d,e}}"
# Output: ["ac","ad","ae","bc","bd","be"]
# 
# 
# 
# Example 2:
# 
# 
# Input: "{{a,z},a{b,c},{ab,z}}"
# Output: ["a","ab","ac","z"]
# Explanation: Each distinct word is written only once in the final
# answer.
# 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= expression.length <= 60
# expression[i] consists of '{', '}', ','or lowercase English letters.
# The given expression represents a set of words based on the grammar given in
# the description.
# 
# 
# 
# 
#

# @lc code=start
import itertools

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        # groups, level = [[]], 0

        # for i, c in enumerate(expression):
        #     if c == '{':
        #         if level == 0:
        #             start = i + 1
        #         level += 1
        #     elif c == '}':
        #         level -= 1
        #         if level == 0:
        #             groups[-1].append(self.braceExpansionII(expression[start:i]))
        #     elif c == ',' and level == 0:
        #         groups.append([])
        #     elif level == 0:
        #         groups[-1].append([c])

        # word_set = set()
        # for group in groups:
        #     word_set |= set(map("".join, itertools.product(*group)))
        # return sorted(word_set)


        stack, res, cur = [], [], []
        for i in range(len(expression)):
            v = expression[i]
            if v.isalpha():
                cur = [c + v for c in cur or [""]]
            elif v == '{':
                stack.append(res)
                stack.append(cur)
                res, cur = [], []
            elif v == '}':
                pre = stack.pop()
                preRes = stack.pop()
                cur = [p + c for c in res + cur for p in pre or [""]]
                res = preRes
            elif v == ',':
                res += cur
                cur = []

        return sorted(set(res + cur))

        
# @lc code=end

