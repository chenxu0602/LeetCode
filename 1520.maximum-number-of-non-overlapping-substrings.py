#
# @lc app=leetcode id=1520 lang=python3
#
# [1520] Maximum Number of Non-Overlapping Substrings
#
# https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/description/
#
# algorithms
# Hard (31.20%)
# Likes:    196
# Dislikes: 32
# Total Accepted:    3.7K
# Total Submissions: 11.8K
# Testcase Example:  '"adefaddaccc"'
#
# Given a string s of lowercase letters, you need to find the maximum number of
# non-empty substrings of s that meet the following conditions:
# 
# 
# The substrings do not overlap, that is for any two substrings s[i..j] and
# s[k..l], either j < k or i > l is true.
# A substring that contains a certain character c must also contain all
# occurrences of c.
# 
# 
# Find the maximum number of substrings that meet the above conditions. If
# there are multiple solutions with the same number of substrings, return the
# one with minimum total length. It can be shown that there exists a unique
# solution of minimum total length.
# 
# Notice that you can return the substrings in any order.
# 
# 
# Example 1:
# 
# 
# Input: s = "adefaddaccc"
# Output: ["e","f","ccc"]
# Explanation: The following are all the possible substrings that meet the
# conditions:
# [
# "adefaddaccc"
# "adefadda",
# "ef",
# "e",
# ⁠ "f",
# "ccc",
# ]
# If we choose the first string, we cannot choose anything else and we'd get
# only 1. If we choose "adefadda", we are left with "ccc" which is the only one
# that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not
# optimal to choose "ef" since it can be split into two. Therefore, the optimal
# way is to choose ["e","f","ccc"] which gives us 3 substrings. No other
# solution of the same number of substrings exist.
# 
# 
# Example 2:
# 
# 
# Input: s = "abbaccd"
# Output: ["d","bb","cc"]
# Explanation: Notice that while the set of substrings ["d","abba","cc"] also
# has length 3, it's considered incorrect since it has larger total length.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s contains only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:

        fst = { c : s.index(c) for c in set(s) }
        lst = { c : s.rindex(c) for c in set(s) }
        
        intervals = []
        for c in set(s):
            b, e = fst[c], lst[c]
            i = b
            while i <= e:
                b = min(b, fst[s[i]])
                e = max(e, lst[s[i]])
                i += 1
            if b == fst[c]:
                intervals.append((e, b))
        
        intervals.sort()
        ans, prev = [], -1
        for e, b in intervals:
            if b > prev:
                ans.append(s[b:e + 1])
                prev = e
        
        return ans

        



        
# @lc code=end

