#
# @lc app=leetcode id=159 lang=python3
#
# [159] Longest Substring with At Most Two Distinct Characters
#
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/
#
# algorithms
# Medium (48.59%)
# Likes:    768
# Dislikes: 14
# Total Accepted:    94.3K
# Total Submissions: 194K
# Testcase Example:  '"eceba"'
#
# Given a string s , find the length of the longest substring t  that contains
# at most 2 distinct characters.
# 
# Example 1:
# 
# 
# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
# 
# 
# Example 2:
# 
# 
# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.
# 
# 
#

# @lc code=start
from collections import defaultdict, OrderedDict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        # n = len(s)
        # if n < 3: return n

        # left, right, max_len = 0, 0, 2
        # hashmap = defaultdict(int)

        # while right < n:
        #     if len(hashmap) < 3:
        #         hashmap[s[right]] = right
        #         right += 1

        #     if len(hashmap) == 3:
        #         del_idx = min(hashmap.values())
        #         del hashmap[s[del_idx]]

        #         left = del_idx + 1

        #     max_len = max(max_len, right - left)

        # return max_len


        queue, start, r, k = OrderedDict(), 0, 0, 2

        for i, char in enumerate(s):
            if char in queue:
                queue.pop(char)
            queue[char] = i

            if len(queue) > k:
                start = queue.popitem(False)[1] + 1

            r = max(r, i - start + 1)

        return r

        
# @lc code=end

