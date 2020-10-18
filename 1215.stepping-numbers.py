#
# @lc app=leetcode id=1215 lang=python3
#
# [1215] Stepping Numbers
#
# https://leetcode.com/problems/stepping-numbers/description/
#
# algorithms
# Medium (37.83%)
# Likes:    69
# Dislikes: 4
# Total Accepted:    3.4K
# Total Submissions: 9K
# Testcase Example:  '0\n21'
#
# A Stepping Number is an integer such that all of its adjacent digits have an
# absolute difference of exactly 1. For example, 321 is a Stepping Number while
# 421 is not.
# 
# Given two integers low and high, find and return a sorted list of all the
# Stepping Numbers in the range [low, high] inclusive.
# 
# 
# Example 1:
# Input: low = 0, high = 21
# Output: [0,1,2,3,4,5,6,7,8,9,10,12,21]
# 
# 
# Constraints:
# 
# 
# 0 <= low <= high <= 2 * 10^9
# 
# 
#

# @lc code=start
from collections import deque
from functools import lru_cache

class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        # @lru_cache(None)
        # def dfs(n):
        #     if n > high:
        #         return
        #     if n >= low:
        #         q.add(n)
        #     d = n % 10
        #     if d == 0:
        #         dfs(n * 10 + 1)
        #     elif d == 9:
        #         dfs(n * 10 + 8)
        #     else:
        #         dfs(n * 10 + d + 1)
        #         dfs(n * 10 + d - 1)

        # q = set()
        # for i in range(10):
        #     dfs(i)
        # return sorted(q)


        def bfs(low, high, num, lst):
            q = deque([num])
            while q:
                neigh = []
                for i in range(len(q)):
                    cur = q.popleft()

                    if low <= cur <= high:
                        lst.append(cur)

                    if cur == 0 or cur > high:
                        continue

                    lastD = cur % 10
                    nei1 = cur * 10 + lastD - 1
                    nei2 = cur * 10 + lastD + 1

                    if lastD == 0:
                        neigh.append(nei2)
                    elif lastD == 9:
                        neigh.append(nei1)
                    else:
                        neigh.append(nei1)
                        neigh.append(nei2)

                q.extend(neigh)


        lst = []
        for i in range(10):
            bfs(low, high, i, lst)
        lst.sort()
        return lst
        
# @lc code=end

