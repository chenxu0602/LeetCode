#
# @lc app=leetcode id=1371 lang=python3
#
# [1371] Find the Longest Substring Containing Vowels in Even Counts
#
# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/
#
# algorithms
# Medium (61.59%)
# Likes:    490
# Dislikes: 18
# Total Accepted:    10.1K
# Total Submissions: 16.3K
# Testcase Example:  '"eleetminicoworoep"'
#
# Given the string s, return the size of the longest substring containing each
# vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must
# appear an even number of times.
# 
# 
# Example 1:
# 
# 
# Input: s = "eleetminicoworoep"
# Output: 13
# Explanation: The longest substring is "leetminicowor" which contains two each
# of the vowels: e, i and o and zero of the vowels: a and u.
# 
# 
# Example 2:
# 
# 
# Input: s = "leetcodeisgreat"
# Output: 5
# Explanation: The longest substring is "leetc" which contains two e's.
# 
# 
# Example 3:
# 
# 
# Input: s = "bcbcbc"
# Output: 6
# Explanation: In this case, the given string "bcbcbc" is the longest because
# all vowels: a, e, i, o and u appear zero times.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 5 x 10^5
# s contains only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        seen = {0: -1}
        res = cur = 0

        for i, c in enumerate(s):
            cur ^= 1 << ("aeiou".find(c) + 1) >> 1
            seen.setdefault(cur, i)
            res = max(res, i - seen[cur])

        return res


        # vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        # d, n, r = {0: -1}, 0, 0

        # for i, c in enumerate(s):
        #     if c in vowels:
        #         n ^= vowels[c]
        #     if n not in d:
        #         d[n] = i
        #     else:
        #         r = max(r, i - d[n])

        # return r
        
# @lc code=end

