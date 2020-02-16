#
# @lc app=leetcode id=340 lang=python3
#
# [340] Longest Substring with At Most K Distinct Characters
#
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
#
# algorithms
# Hard (39.80%)
# Likes:    546
# Dislikes: 18
# Total Accepted:    76.5K
# Total Submissions: 191.6K
# Testcase Example:  '"eceba"\n2'
#
# Given a string, find the length of the longest substring T that contains at
# most k distinct characters.
# 
# Example 1:
# 
# 
# 
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.
# 
# 
# 
#
from collections import OrderedDict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        # d = {}
        # res, low = 0, 0
        # for i, c in enumerate(s):
        #     d[c] = i
        #     if len(d) > k:
        #         low = min(d.values())
        #         del d[s[low]]
        #         low += 1
        #     res = max(res, i - low + 1)
        # return res

        n = len(s)
        if k == 0 or n == 0:
            return 0

        left, right = 0, 0
        hashmap = OrderedDict()

        max_len = 1

        while right < n:
            character = s[right]

            if character in hashmap:
                del hashmap[character]

            hashmap[character] = right
            right += 1

            if len(hashmap) == k + 1:
                _, del_idx = hashmap.popitem(last=False)
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len





        

