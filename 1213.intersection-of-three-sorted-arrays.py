#
# @lc app=leetcode id=1213 lang=python3
#
# [1213] Intersection of Three Sorted Arrays
#
# https://leetcode.com/problems/intersection-of-three-sorted-arrays/description/
#
# algorithms
# Easy (77.31%)
# Likes:    81
# Dislikes: 5
# Total Accepted:    11.7K
# Total Submissions: 15.1K
# Testcase Example:  '[1,2,3,4,5]\n[1,2,5,7,9]\n[1,3,4,5,8]'
#
# Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing
# order, return a sorted array of only the integers that appeared in all three
# arrays.
# 
# 
# Example 1:
# 
# 
# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# Output: [1,5]
# Explanation: Only 1 and 5 appeared in the three arrays.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr1.length, arr2.length, arr3.length <= 1000
# 1 <= arr1[i], arr2[i], arr3[i] <= 2000
# 
# 
#

# @lc code=start
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        i = j = k = 0
        res = []

        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                res.append(arr1[i])
                i, j, k = i + 1, j + 1, k + 1
                continue

            max_ = max(arr1[i], arr2[j], arr3[k])
            if arr1[i] < max_:
                i += 1
            if arr2[j] < max_:
                j += 1
            if arr3[k] < max_:
                k += 1

        return res
        
# @lc code=end

