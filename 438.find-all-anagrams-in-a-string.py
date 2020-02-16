#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (40.11%)
# Likes:    2163
# Dislikes: 156
# Total Accepted:    176.7K
# Total Submissions: 440.2K
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

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def countarr(w):
            out = [0] * 26
            for c in w:
                out[ord(c) - ord('a')] += 1
            return out

        ps = countarr(p)
        res = []
        ss = countarr(s[:len(p)])

        if ss == ps:
            res = [0]

        for i in range(1, len(s) - len(p) + 1):
            left = ord(s[i-1]) - ord('a')
            right = ord(s[i+len(p)-1]) - ord('a')

            ss[left] -= 1
            ss[right] += 1

            if ss == ps:
                res.append(i)

        return res

        
# @lc code=end

