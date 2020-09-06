#
# @lc app=leetcode id=828 lang=python3
#
# [828] Count Unique Characters of All Substrings of a Given String
#
# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/description/
#
# algorithms
# Hard (44.89%)
# Likes:    433
# Dislikes: 43
# Total Accepted:    10.8K
# Total Submissions: 23.7K
# Testcase Example:  '"ABC"'
#
# Let's define a function countUniqueChars(s) that returns the number of unique
# characters on s, for example if s = "LEETCODE" then "L", "T","C","O","D" are
# the unique characters since they appear only once in s, therefore
# countUniqueChars(s) = 5.
# 
# On this problem given a string s we need to return the sum of
# countUniqueChars(t) where t is a substring of s. Notice that some substrings
# can be repeated so on this case you have to count the repeated ones too.
# 
# Since the answer can be very large, return the answer modulo 10 ^ 9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: s = "ABC"
# Output: 10
# Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
# Evey substring is composed with only unique letters.
# Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
# 
# 
# Example 2:
# 
# 
# Input: s = "ABA"
# Output: 8
# Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "LEETCODE"
# Output: 92
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 10^4
# s contain upper-case English letters only.
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # N, index, peek = len(s), defaultdict(list), defaultdict(int)
        # for i, c in enumerate(s):
        #     index[c].append(i)
        # for c in index:
        #     index[c].extend([N, N])

        # def get(c):
        #     return index[c][peek[c] + 1] - index[c][peek[c]]

        # ans = 0
        # cur = sum(get(c) for c in index)
        # for i, c in enumerate(s):
        #     ans += cur
        #     oldv = get(c)
        #     peek[c] += 1
        #     cur += get(c) - oldv

        # return ans % (10**9 + 7)


        index = defaultdict(list)
        for i, c in enumerate(s):
            index[c].append(i)

        ans = 0
        for A in index.values():
            A = [-1] + A + [len(s)]
            for i in range(1, len(A) - 1):
                ans += (A[i] - A[i - 1]) * (A[i + 1] - A[i])

        return ans % (10**9 + 7)
        
# @lc code=end

