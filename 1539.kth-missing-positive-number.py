#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#
# https://leetcode.com/problems/kth-missing-positive-number/description/
#
# algorithms
# Easy (53.40%)
# Likes:    382
# Dislikes: 11
# Total Accepted:    24.4K
# Total Submissions: 45.7K
# Testcase Example:  '[2,3,4,7,11]\n5'
#
# Given an array arr of positive integers sorted in a strictly increasing
# order, and an integer k.
# 
# Find the k^th positive integer that is missing from this array.
# 
# 
# Example 1:
# 
# 
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The
# 5^th missing positive integer is 9.
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2^nd missing
# positive integer is 6.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# arr[i] < arr[j] for 1 <= i < j <= arr.length
# 
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Brute Force, O(N) time
        # if k <= arr[0] - 1:
        #     return k
        # k -= arr[0] - 1

        # for i in range(len(arr) - 1):
        #     curr_missing = arr[i + 1] - arr[i] - 1
        #     if k <= curr_missing:
        #         return arr[i] + k

        #     k -= curr_missing

        # return arr[-1] + k


        # Binary Search, O(logN) time
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot = (left + right) // 2
            # If number of positive integers
            # which are missing before arr[pivot]
            # is less than k -->
            # continue to search on the right.
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            # Otherwise, go left.
            else:
                right = pivot - 1

        # At the end of the loop, left = right + 1,
        # and the kth missing is in-between arr[right] and arr[left].
        # The number of integers missing before arr[right] is
        # arr[right] - right - 1 -->
        # the number to return is
        # arr[right] + k - (arr[right] - right - 1) = k + left
        return left + k

        

        
# @lc code=end

