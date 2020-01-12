#
# @lc app=leetcode id=556 lang=python3
#
# [556] Next Greater Element III
#
# https://leetcode.com/problems/next-greater-element-iii/description/
#
# algorithms
# Medium (30.11%)
# Likes:    375
# Dislikes: 122
# Total Accepted:    27.6K
# Total Submissions: 91.4K
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
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if not n: return -1
        
        s = str(n)
        arr = [c for c in s]
        i = len(arr) - 1
        while i > 0:
            prev = int(arr[i-1])
            if int(arr[i]) > prev:
                j = i
                while j < len(arr) and int(arr[j]) > prev:
                    j += 1
                arr[i-1], arr[j-1], j = arr[j-1], arr[i-1], len(arr) - 1

                """
                while i < j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
                """

                arr[i:] = sorted(arr[i:])

                res = int("".join(arr))


                return -1 if res > 2147483647 else res
            i -= 1
        return -1
        

