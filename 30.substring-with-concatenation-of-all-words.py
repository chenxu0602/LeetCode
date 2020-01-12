#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (23.98%)
# Likes:    640
# Dislikes: 1024
# Total Accepted:    148.9K
# Total Submissions: 613.9K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string, s, and a list of words, words, that are all of the
# same length. Find all starting indices of substring(s) in s that is a
# concatenation of each word in words exactly once and without any intervening
# characters.
# 
# Example 1:
# 
# 
# Input:
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
# 
# 
# Example 2:
# 
# 
# Input:
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# Output: []
# 
# 
#

# @lc code=start
from collections import defaultdict, Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        if not words:
            return []

        n = len(words)
        wl = len(words[0])

        frequency = Counter(words)

        results = []

        for i in range(len(s) - n * wl + 1):
            j, seen = 0, defaultdict(int)

            while j < n:
                start_loc = i + j * wl
                sub_str = s[start_loc:start_loc+wl]

                if sub_str not in frequency:
                    break
                else:
                    seen[sub_str] += 1
                    if seen[sub_str] > frequency[sub_str]:
                        break
                j += 1
            if j == n:
                results.append(i)

        return results

        
# @lc code=end

