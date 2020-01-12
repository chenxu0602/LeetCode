#
# @lc app=leetcode id=267 lang=python3
#
# [267] Palindrome Permutation II
#
# https://leetcode.com/problems/palindrome-permutation-ii/description/
#
# algorithms
# Medium (33.71%)
# Likes:    250
# Dislikes: 34
# Total Accepted:    26.6K
# Total Submissions: 78.8K
# Testcase Example:  '"aabb"'
#
# Given a string s, return all the palindromic permutations (without
# duplicates) of it. Return an empty list if no palindromic permutation could
# be form.
# 
# Example 1:
# 
# 
# Input: "aabb"
# Output: ["abba", "baab"]
# 
# Example 2:
# 
# 
# Input: "abc"
# Output: []
# 
#
from collections import Counter
from itertools import permutations

class Solution:
    def permute(self, s: list, l: int, ch: str) -> None:
        if l == len(s):
            self.res.append("".join(s + [ch] + s[::-1]))
        else:
            for i in range(l, len(s)):
                if i == l or not s[i] == s[l]:
                    s[i], s[l] = s[l], s[i]
                    self.permute(s, l + 1, ch)
                    s[i], s[l] = s[l], s[i]


    def generatePalindromes(self, s: str) -> List[str]:
        """
        d = Counter(s)
        m = tuple(k for k, v in d.items() if v % 2)
        p = "".join(k * (v // 2) for k, v in d.items())
        p = list(p)

        if len(m) > 1:
            return []

#        return sorted(["".join(permute + m + permute[::-1]) for permute in set(permutations(p))])

        self.res = []
        self.permute(p, 0, m[0] if m else "")

        return list(set(self.res))
        """

        d = Counter(s)
        m = tuple(k for k, v in d.items() if v % 2)
        p = "".join(k * (v // 2) for k, v in d.items())
#        return ["".join(i + m + i[::-1]) for i in set(permutations(p))] if len(m) < 2 else []


        if len(m) > 1:
            return []

        self.res = []
        self.permute(list(p), 0, m[0] if m else "")

        return list(set(self.res))
        



        

        
        

