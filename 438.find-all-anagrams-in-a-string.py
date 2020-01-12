#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Easy (37.57%)
# Likes:    1652
# Dislikes: 129
# Total Accepted:    130.5K
# Total Submissions: 347.2K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
# 
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
# 
# The order of output does not matter.
# 
# Example 1:
# 
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# 
# Example 2:
# 
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
#
class Solution:
    def countarr(self, w):
        out = [0] * 26
        for c in w:
            out[ord(c) - ord('a')] += 1
        return out

    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(p)
        ps = self.countarr(p)
        ans = []
        ss =self.countarr(s[:m])

        if ss == ps:
            ans = [0]

        for i in range(1, len(s)-m+1):
            left = ord(s[i-1]) - ord('a')
            right = ord(s[i+m-1]) - ord('a')

            ss[left] -= 1
            ss[right] += 1

            if ss == ps:
                ans.append(i)

        return ans
        

