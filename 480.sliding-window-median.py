#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#
# https://leetcode.com/problems/sliding-window-median/description/
#
# algorithms
# Hard (35.11%)
# Likes:    627
# Dislikes: 63
# Total Accepted:    39.2K
# Total Submissions: 111.5K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# Examples:
# 
# [2,3,4] , the median is 3
# 
# [2,3], the median is (2 + 3) / 2 = 2.5
# 
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position. Your
# job is to output the median array for each window in the original array.
# 
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
# 
# 
# Window position                Median
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
# ⁠1 [3  -1  -3] 5  3  6  7       -1
# ⁠1  3 [-1  -3  5] 3  6  7       -1
# ⁠1  3  -1 [-3  5  3] 6  7       3
# ⁠1  3  -1  -3 [5  3  6] 7       5
# ⁠1  3  -1  -3  5 [3  6  7]      6
# 
# 
# Therefore, return the median sliding window as [1,-1,-1,3,5,6].
# 
# Note: 
# You may assume k is always valid, ie: k is always smaller than input array's
# size for non-empty array.
# Answers within 10^-5 of the actual value will be accepted as correct.
# 
#

# @lc code=start
import bisect, heapq

class Solution:
    def calc_median(self, max_heap, min_heap):
        return min_heap[0] if len(min_heap) > len(max_heap) \
            else 0.5 * (min_heap[0] - max_heap[0])

    def add_to_heaps(self, max_heap, min_heap, num):
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, num))
        if len(min_heap) < len(max_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

    def remove_from_heap(self, heap, num):
        index = heap.index(num)
        heap[index] = heap[-1]
        heap.pop()

        if index < len(heap):
            heapq._siftup(heap, index)
            heapq._siftdown(heap, 0, index)

    def remove_from_heaps(self, max_heap, min_heap, num):
        if min_heap[0] <= num:
            self.remove_from_heap(min_heap, num)
            return
        self.remove_from_heap(max_heap, -num)


    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        # Time  complexity: O(nklogk) to O(nk)
        # Space complexity: O(k)
        # medians, window = [], []
        # for i in range(len(nums)):
        #     if i >= k:
        #         window.pop(bisect.bisect_right(window, nums[i-k]) - 1)
        #     bisect.insort(window, nums[i])

        #     if i >= k - 1:
        #         medians.append(float(window[k//2]) if k & 1 > 0 else 
        #         0.5 * (window[k//2-1] + window[k//2]))
        # return medians


        max_heap, min_heap, result = [], [], []

        for i in range(k-1):
            self.add_to_heaps(max_heap, min_heap, nums[i])

        for i in range(k-1, len(nums)):
            self.add_to_heaps(max_heap, min_heap, nums[i])
            median = self.calc_median(max_heap, min_heap)
            result.append(median)
            self.remove_from_heaps(max_heap, min_heap, nums[i-k+1])

        return result
        
# @lc code=end

