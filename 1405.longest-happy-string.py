#
# @lc app=leetcode id=1405 lang=python3
#
# [1405] Longest Happy String
#
# https://leetcode.com/problems/longest-happy-string/description/
#
# algorithms
# Medium (50.44%)
# Likes:    410
# Dislikes: 86
# Total Accepted:    14.7K
# Total Submissions: 28.4K
# Testcase Example:  '1\n1\n7'
#
# A string is called happy if it does not have any of the strings 'aaa', 'bbb'
# or 'ccc' as a substring.
# 
# Given three integers a, b and c, return any string s, which satisfies
# following conditions:
# 
# 
# s is happy and longest possible.
# s contains at most a occurrences of the letter 'a', at most b occurrences of
# the letter 'b' and at most c occurrences of the letter 'c'.
# s will only contain 'a', 'b' and 'c' letters.
# 
# 
# If there is no such string s return the empty string "".
# 
# 
# Example 1:
# 
# 
# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
# 
# 
# Example 2:
# 
# 
# Input: a = 2, b = 2, c = 1
# Output: "aabbc"
# 
# 
# Example 3:
# 
# 
# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It's the only correct answer in this case.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= a, b, c <= 100
# a + b + c > 0
# 
# 
#

# @lc code=start
import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0: heap.append([-a, 'a'])
        if b > 0: heap.append([-b, 'b'])
        if c > 0: heap.append([-c, 'c'])
        heapq.heapify(heap)

        res = ""
        while len(heap) > 1:
            a, b = heapq.heappop(heap), heapq.heappop(heap)

            if a[0] < -1 and not (len(res) >= 1 and res[-1] == a[1]):
                res += a[1] * 2
                a[0] += 2
            else:
                res += a[1]
                a[0] += 1

            res += b[1]
            b[0] += 1

            if a[0] < 0:
                heapq.heappush(heap, a)

            if b[0] < 0:
                heapq.heappush(heap, b)

        if heap:
            if len(res) >= 2 and res[-1] == res[-2] == heap[0][1] and heap[0][0] < 0:
                pass
            elif len(res) >= 1 and res[-1] == heap[0][1] and heap[0][0] < 0:
                res += heap[0][1]
            else:
                res += heap[0][1] * min(2, -heap[0][0])

        return res


        
# @lc code=end

