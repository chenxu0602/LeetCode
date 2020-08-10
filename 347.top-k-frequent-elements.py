#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (55.05%)
# Likes:    1575
# Dislikes: 97
# Total Accepted:    211.6K
# Total Submissions: 383.3K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given a non-empty array of integers, return the k most frequent elements.
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Note: 
# 
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
# 
# 
#

from collections import Counter
import heapq
import random

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = Counter(nums).most_common(k)
        # return [i[0] for i in count]

        # Bubble Sort
        # count = list(Counter(nums).items())
        # for j in range(k):
        #     for i in range(len(count) - j - 1):
        #         if count[i][1] > count[i+1][1]:
        #             count[i], count[i+1] = count[i+1], count[i]

        # return [x for x, y in count[len(count)-k:]]


        # Heap
        # Time  complexity: O(Nlogk)
        # Space complexity: O(N + k)
        # if k == len(nums): return nums
        # count = Counter(nums)
        # return heapq.nlargest(k, count.keys(), key=count.get)


        # Quickselect
        # Time  complexity: O(N) in the average case, O(N^2) in the worst case.
        # Space complexity: O(N)
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index

        def quickselect(left, right, k_smallest) -> None:
            if left == right: return

            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            if k_smallest == pivot_index:
                return
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            else:
                quickselect(pivot_index + 1, right, k_smallest)


        n = len(unique)
        quickselect(0, n - 1, n - k)
        return unique[n - k:]
            



