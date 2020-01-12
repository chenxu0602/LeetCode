#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#
# https://leetcode.com/problems/interval-list-intersections/description/
#
# algorithms
# Medium (63.76%)
# Likes:    478
# Dislikes: 18
# Total Accepted:    34K
# Total Submissions: 53.1K
# Testcase Example:  '[[0,2],[5,10],[13,23],[24,25]]\n[[1,5],[8,12],[15,24],[25,26]]'
#
# Given two lists of closed intervals, each list of intervals is pairwise
# disjoint and in sorted order.
# 
# Return the intersection of these two interval lists.
# 
# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real
# numbers x with a <= x <= b.  The intersection of two closed intervals is a
# set of real numbers that is either empty, or can be represented as a closed
# interval.  For example, the intersection of [1, 3] and [2, 4] is [2,
# 3].)
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Reminder: The inputs and the desired output are lists of Interval objects,
# and not arrays or lists.
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= A.length < 1000
# 0 <= B.length < 1000
# 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
# 
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
# 
#
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        ans = []
        i = j = 0

        while i < len(A) and j < len(B):

            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])

            if lo <= hi:
                ans.append([lo, hi])

            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans

        """

        if not A or not B:
            return []

        a, b, s, ret = [], [], [], []
        A.reverse()
        B.reverse()

        while (A or a) and (B or b):
            if not a:
                a = A.pop()
                a = [a[1], a[0]]

            if not b:
                b = B.pop()
                b = [b[1], b[0]]

            c = a
            if a[-1] < b[-1]:
                c = a
            elif a[-1] > b[-1]:
                c = b
            else:
                c = a if len(a) == 2 else b

            if len(c) == 2:
                s.append(c.pop())
            else:
                num = s.pop()
                num_end = c.pop()
                if len(s):
                    ret.append([num, num_end])
                else:
                    pass
        return ret
        """

