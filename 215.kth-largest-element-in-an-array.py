#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (52.13%)
# Likes:    2895
# Dislikes: 209
# Total Accepted:    518.8K
# Total Submissions: 994.2K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#

# @lc code=start
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # Heap
        # Time  complexity: O(Nlogk)
        # Space complexity: O(k)
        # return heapq.nlargest(k, nums)[-1]

        # QuickSelect
        # Time  complexity: O(N) on average, O(N^2) in the worse case.
        # Space complexity: O(1)
        def partition(nums, low, high):
            i = low
            pivot = nums[high]

            for j in range(low, high):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            nums[i], nums[high] = nums[high], nums[i]
            return i

        def findKthSmallest(nums, k):
            if nums:
                pos = partition(nums, 0, len(nums) - 1)
                if k > pos + 1:
                    return findKthSmallest(nums[pos+1:], k - pos - 1)
                elif k < pos + 1:
                    return findKthSmallest(nums[:pos], k)
                else:
                    return nums[pos]

        return findKthSmallest(nums, len(nums) - (k - 1))
        

        
# @lc code=end

