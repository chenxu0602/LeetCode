#
# @lc app=leetcode id=267 lang=python3
#
# [267] Palindrome Permutation II
#
# https://leetcode.com/problems/palindrome-permutation-ii/description/
#
# algorithms
# Medium (36.32%)
# Likes:    449
# Dislikes: 52
# Total Accepted:    38.1K
# Total Submissions: 104.7K
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

# @lc code=start
from collections import Counter

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        # Backtracking
        # Time  complexity: O((n/2 + 1)!)
        # Space complexity: O(n)
        def permute(s, l, ch):
            if l == len(s):
                res.append("".join(s + [ch] + s[::-1]))
            else:
                for i in range(l, len(s)):
                    if i == l or not s[i] == s[l]:
                        s[i], s[l] = s[l], s[i]
                        permute(s, l + 1, ch)
                        s[i], s[l] = s[l], s[i]

        d = Counter(s)
        m = tuple(k for k, v in d.items() if v % 2)
        p = "".join(k * (v // 2) for k, v in d.items())

        if len(m) > 1: return []

        res = []
        permute(list(p), 0, m[0] if m else "")
        return list(set(res))

        
# @lc code=end

