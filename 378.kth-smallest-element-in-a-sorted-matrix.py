#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (52.03%)
# Likes:    1765
# Dislikes: 106
# Total Accepted:    152K
# Total Submissions: 291.9K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# Given a n x n matrix where each of the rows and columns are sorted in
# ascending order, find the kth smallest element in the matrix.
# 
# 
# Note that it is the kth smallest element in the sorted order, not the kth
# distinct element.
# 
# 
# Example:
# 
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
# 
# return 13.
# 
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ n^2.
#

# @lc code=start
import heapq
import itertools

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        # return next(itertools.islice(heapq.merge(*matrix), k - 1, k))


        # Min-Heap approach
        # Time  complexity: O(X + KlogX), where X = min(K, N)
        # Space complexity: O(X)
        # N = len(matrix)
        # # Preparing our min-heap
        # minHeap = []
        # for r in range(min(k, N)):
        #     # We add triplets of information for each cell
        #     minHeap.append((matrix[r][0], r, 0))

        # # Heapify our list
        # heapq.heapify(minHeap)

        # # Until we find k elements
        # while k:
        #     element, r, c = heapq.heappop(minHeap)
        #     # If we have any new elements in the current row, add them
        #     if c < N - 1:
        #         heapq.heappush(minHeap, (matrix[r][c + 1], r, c + 1))

        #     k -= 1

        # return element


        # Binary Search
        # Time  complexity: O(N x log(Max - Min))
        # Space complexity: O(1)
        def countLessEqual(matrix, mid, smaller, larger):
            count, n = 0, len(matrix)
            row, col = n - 1, 0

            while row >= 0 and col < n:
                if matrix[row][col] > mid:
                    larger = min(larger, matrix[row][col])
                    row -= 1
                else:
                    smaller = max(smaller, matrix[row][col])
                    count += row + 1
                    col += 1

            return count, smaller, larger

        n = len(matrix)
        start, end = matrix[0][0], matrix[n - 1][n - 1]
        while start < end:
            mid = start + (end - start) // 2
            smaller, larger = matrix[0][0], matrix[n - 1][n - 1]

            count, smaller, larger = countLessEqual(matrix, mid, smaller, larger)

            if count == k:
                return smaller
            elif count < k:
                start = larger # search higher
            else:
                end = smaller   # search lower

        return start

        
# @lc code=end

