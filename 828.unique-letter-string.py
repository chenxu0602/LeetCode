#
# @lc app=leetcode id=828 lang=python3
#
# [828] Unique Letter String
#
# https://leetcode.com/problems/unique-letter-string/description/
#
# algorithms
# Hard (40.77%)
# Likes:    249
# Dislikes: 30
# Total Accepted:    6.3K
# Total Submissions: 15.2K
# Testcase Example:  '"ABC"'
#
# A character is unique in string S if it occurs exactly once in it.
# 
# For example, in string S = "LETTER", the only unique characters are "L" and
# "R".
# 
# Let's define UNIQ(S) as the number of unique characters in string S.
# 
# For example, UNIQ("LETTER") =  2.
# 
# Given a string S with only uppercases, calculate the sum of UNIQ(substring)
# over all non-empty substrings of S.
# 
# If there are two or more equal substrings at different positions in S, we
# consider them different.
# 
# Since the answer can be very large, return the answer modulo 10 ^ 9 + 7.
# 
# 
# 
# Example 1:
# 
# 
# Input: "ABC"
# Output: 10
# Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
# Evey substring is composed with only unique letters.
# Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
# 
# Example 2:
# 
# 
# Input: "ABA"
# Output: 8
# Explanation: The same as example 1, except uni("ABA") = 1.
# 
# 
# 
# 
# Note: 0 <= S.length <= 10000.
# 
#
from collections import defaultdict
class Solution:
    def uniqueLetterString(self, S: str) -> int:
        """
        N = len(S)
        index = defaultdict(list)
        peek = defaultdict(int)

        for i, c in enumerate(S):
            index[c].append(i)

        for c in index:
            index[c].extend([N, N])

        def get(c):
            return index[c][peek[c] + 1] - index[c][peek[c]]

        ans = 0
        cur = sum(get(c) for c in index)

        for i, c in enumerate(S):
            ans += cur
            oldv = get(c)
            peek[c] += 1
            cur += get(c) - oldv
        return ans % (10**9 + 7)
        """

        index = defaultdict(list)
        for i, c in enumerate(S):
            index[c].append(i)

        ans = 0
        for A in index.values():
            A = [-1] + A + [len(S)]
            for i in range(1, len(A) - 1):
                ans += (A[i] - A[i-1]) * (A[i+1] - A[i])
        return ans % (10**9 + 7)

        

