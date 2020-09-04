#
# @lc app=leetcode id=761 lang=python3
#
# [761] Special Binary String
#
# https://leetcode.com/problems/special-binary-string/description/
#
# algorithms
# Hard (54.55%)
# Likes:    315
# Dislikes: 105
# Total Accepted:    8.2K
# Total Submissions: 14.9K
# Testcase Example:  '"11011000"'
#
# 
# Special binary strings are binary strings with the following two properties:
# 
# The number of 0's is equal to the number of 1's.
# Every prefix of the binary string has at least as many 1's as 0's.
# 
# Given a special string S, a move consists of choosing two consecutive,
# non-empty, special substrings of S, and swapping them.  (Two strings are
# consecutive if the last character of the first string is exactly one index
# before the first character of the second string.)
# 
# At the end of any number of moves, what is the lexicographically largest
# resulting string possible?
# 
# 
# Example 1:
# 
# Input: S = "11011000"
# Output: "11100100"
# Explanation:
# The strings "10" [occuring at S[1]] and "1100" [at S[3]] are swapped.
# This is the lexicographically largest string possible after some number of
# swaps.
# 
# 
# 
# Note:
# S has length at most 50.
# S is guaranteed to be a special binary string as defined above.
# 
#

# @lc code=start
class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        # 1. Split S into several special strings (as many as possible).
        # 2. Special string starts with 1 and ends with 0. Recursion on the middle part.
        # 3. Sort all special strings in lexicographically largest order.
        # 4. Join and output all strings.
        # Time  complexity: O(N^2)
        # Space compleixty: O(N)
        if not S: return S
        mountains, anchor, bal = [], 0, 0
        for i, x in enumerate(S):
            bal += 1 if x == '1' else -1
            if bal == 0:
                mountains.append("1{}0".format(self.makeLargestSpecial(S[anchor + 1:i])))
                anchor = i + 1

        mountains.sort(reverse=True)
        return "".join(mountains)
        
# @lc code=end

