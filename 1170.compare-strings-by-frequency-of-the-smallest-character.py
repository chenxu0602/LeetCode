#
# @lc app=leetcode id=1170 lang=python3
#
# [1170] Compare Strings by Frequency of the Smallest Character
#
# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/description/
#
# algorithms
# Easy (58.61%)
# Likes:    282
# Dislikes: 703
# Total Accepted:    47K
# Total Submissions: 79.3K
# Testcase Example:  '["cbd"]\n["zaaaz"]'
#
# Let's define a function f(s) over a non-empty string s, which calculates the
# frequency of the smallest character in s. For example, if s = "dcce" then
# f(s) = 2 because the smallest character is "c" and its frequency is 2.
# 
# Now, given string arrays queries and words, return an integer array answer,
# where each answer[i] is the number of words such that f(queries[i]) < f(W),
# where W is a word in words.
# 
# 
# Example 1:
# 
# 
# Input: queries = ["cbd"], words = ["zaaaz"]
# Output: [1]
# Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so
# f("cbd") < f("zaaaz").
# 
# 
# Example 2:
# 
# 
# Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# Output: [1,2]
# Explanation: On the first query only f("bbb") < f("aaaa"). On the second
# query both f("aaa") and f("aaaa") are both > f("cc").
# 
# 
# 
# Constraints:
# 
# 
# 1 <= queries.length <= 2000
# 1 <= words.length <= 2000
# 1 <= queries[i].length, words[i].length <= 10
# queries[i][j], words[i][j] are English lowercase letters.
# 
# 
#

# @lc code=start
import bisect

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f = sorted(w.count(min(w)) for w in words)
        return [len(f) - bisect.bisect_right(f, q.count(min(q))) for q in queries]
        
# @lc code=end

