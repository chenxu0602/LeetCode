#
# @lc app=leetcode id=556 lang=python3
#
# [556] Next Greater Element III
#
# https://leetcode.com/problems/next-greater-element-iii/description/
#
# algorithms
# Medium (31.00%)
# Likes:    502
# Dislikes: 153
# Total Accepted:    35K
# Total Submissions: 112.7K
# Testcase Example:  '12'
#
# Given a positive 32-bit integer n, you need to find the smallest 32-bit
# integer which has exactly the same digits existing in the integer n and is
# greater in value than n. If no such positive 32-bit integer exists, you need
# to return -1.
# 
# Example 1:
# 
# 
# Input: 12
# Output: 21
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 21
# Output: -1
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, n: int) -> int:

        s = str(n)
        arr = [c for c in s]
        i = len(arr) - 2

        while i >= 0 and arr[i+1] <= arr[i]:
            i -= 1

        if i < 0: return -1

        j = len(arr) - 1
        while j >= 0 and arr[j] <= arr[i]:
            j -= 1

        arr[i], arr[j] = arr[j], arr[i]

        l, r = i+1, len(arr)-1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1; r -= 1

        res = int("".join(arr))
        return -1 if res > 2**31 - 1 else res
        
# @lc code=end

