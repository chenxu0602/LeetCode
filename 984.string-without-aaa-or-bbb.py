#
# @lc app=leetcode id=984 lang=python3
#
# [984] String Without AAA or BBB
#
# https://leetcode.com/problems/string-without-aaa-or-bbb/description/
#
# algorithms
# Medium (34.44%)
# Likes:    117
# Dislikes: 191
# Total Accepted:    11.9K
# Total Submissions: 34.4K
# Testcase Example:  '1\n2'
#
# Given two integers A and B, return any string S such that:
# 
# 
# S has length A + B and contains exactly A 'a' letters, and exactly B 'b'
# letters;
# The substring 'aaa' does not occur in S;
# The substring 'bbb' does not occur in S.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = 1, B = 2
# Output: "abb"
# Explanation: "abb", "bab" and "bba" are all correct answers.
# 
# 
# 
# Example 2:
# 
# 
# Input: A = 4, B = 1
# Output: "aabaa"
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= A <= 100
# 0 <= B <= 100
# It is guaranteed such an S exists for the given A and B.
# 
# 
#
class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:

        ans = []

        while A or B:
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                writeA = ans[-1] == 'b'
            else:
                writeA = A >= B

            if writeA:
                A -= 1
                ans.append('a')
            else:
                B -= 1
                ans.append('b')

        return "".join(ans)
        

