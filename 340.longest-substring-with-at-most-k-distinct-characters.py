#
# @lc app=leetcode id=340 lang=python3
#
# [340] Longest Substring with At Most K Distinct Characters
#
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
#
# algorithms
# Hard (42.48%)
# Likes:    812
# Dislikes: 26
# Total Accepted:    107.1K
# Total Submissions: 251.8K
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

# @lc code=start
from collections import OrderedDict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Time  complexity: O(N)
        # Space complexity: O(k)
        queue, start, r = OrderedDict(), -1, 0

        for i, char in enumerate(s):
            if char in queue:
                queue.pop(char)
            queue[char] = i

            if len(queue) > k:
                start = queue.popitem(False)[1]

            r = max(r, i - start)

        return r
        
# @lc code=end

