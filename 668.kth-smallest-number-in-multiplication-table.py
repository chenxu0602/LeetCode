#
# @lc app=leetcode id=668 lang=python3
#
# [668] Kth Smallest Number in Multiplication Table
#
# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/description/
#
# algorithms
# Hard (45.47%)
# Likes:    580
# Dislikes: 21
# Total Accepted:    21.5K
# Total Submissions: 46.8K
# Testcase Example:  '3\n3\n5'
#
# 
# Nearly every one have used the Multiplication Table. But could you find out
# the k-th smallest number quickly from the multiplication table?
# 
# 
# 
# Given the height m and the length n of a m * n Multiplication Table, and a
# positive integer k, you need to return the k-th smallest number in this
# table.
# 
# 
# Example 1:
# 
# Input: m = 3, n = 3, k = 5
# Output: 
# Explanation: 
# The Multiplication Table:
# 1    2    3
# 2    4    6
# 3    6    9
# 
# The 5-th smallest number is 3 (1, 2, 2, 3, 3).
# 
# 
# 
# 
# Example 2:
# 
# Input: m = 2, n = 3, k = 6
# Output: 
# Explanation: 
# The Multiplication Table:
# 1    2    3
# 2    4    6
# 
# The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
# 
# 
# 
# 
# Note:
# 
# The m and n will be in the range [1, 30000].
# The k will be in the range [1, m * n]
# 
# 
#

# @lc code=start
import heapq

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # Next Heap
        # Time  complexity: O(k x mlogm) = O(m^2nlogm)
        # Space complexity: O(m)
        # heap = [(i, i) for i in range(1, m + 1)]
        # heapq.heapify(heap)

        # for _ in range(k):
        #     val, root = heapq.heappop(heap)
        #     nxt = val + root
        #     if nxt <= root * n:
        #         heapq.heappush(heap, (nxt, root))

        # return val


        # Binary Search
        # Time  complexity: O(mlogmn)
        # Space complexity: O(1)
        def enough(x):
            count = 0
            for i in range(1, m + 1):
                count += min(x // i, n)
            return count >= k

        lo, hi = 1, m * n
        while lo < hi:
            mi = (lo + hi) // 2
            if not enough(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo
        
# @lc code=end

