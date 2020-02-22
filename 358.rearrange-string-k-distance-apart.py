#
# @lc app=leetcode id=358 lang=python3
#
# [358] Rearrange String k Distance Apart
#
# https://leetcode.com/problems/rearrange-string-k-distance-apart/description/
#
# algorithms
# Hard (32.85%)
# Likes:    257
# Dislikes: 12
# Total Accepted:    22.6K
# Total Submissions: 68.6K
# Testcase Example:  '"aabbcc"\n3'
#
# Given a non-empty string s and an integer k, rearrange the string such that
# the same characters are at least distance k from each other.
# 
# All input strings are given in lowercase letters. If it is not possible to
# rearrange the string, return an empty string "".
# 
# Example 1:
# 
# 
# 
# Input: s = "aabbcc", k = 3
# Output: "abcabc" 
# Explanation: The same letters are at least distance 3 from each other.
# 
# 
# 
# Example 2:
# 
# 
# Input: s = "aaabc", k = 3
# Output: "" 
# Explanation: It is not possible to rearrange the string.
# 
# 
# 
# Example 3:
# 
# 
# Input: s = "aaadbbcc", k = 2
# Output: "abacabcd"
# Explanation: The same letters are at least distance 2 from each other.
# 
# 
# 
# 
#
from collections import Counter, deque
import heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0: return s
        count, ans = Counter(s), []
        heap, q = [(-cnt, c) for c, cnt in count.most_common()], deque()

        while heap:
            cnt, c = heapq.heappop(heap)
            ans += c,
            q.append((cnt + 1, c))
            if len(q) >= k:
                t = q.popleft()
                if t[0] < 0:
                    heapq.heappush(heap, t)

        return "".join(ans) if len(ans) == len(s) else ""
        

