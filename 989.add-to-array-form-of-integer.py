#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#
# https://leetcode.com/problems/add-to-array-form-of-integer/description/
#
# algorithms
# Easy (44.19%)
# Likes:    402
# Dislikes: 69
# Total Accepted:    48K
# Total Submissions: 108K
# Testcase Example:  '[1,2,0,0]\n34'
#
# For a non-negative integer X, the array-form of X is an array of its digits
# in left to right order.  For example, if X = 1231, then the array form is
# [1,2,3,1].
# 
# Given the array-form A of a non-negative integer X, return the array-form of
# the integer X+K.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,2,0,0], K = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234
# 
# 
# 
# Example 2:
# 
# 
# Input: A = [2,7,4], K = 181
# Output: [4,5,5]
# Explanation: 274 + 181 = 455
# 
# 
# 
# Example 3:
# 
# 
# Input: A = [2,1,5], K = 806
# Output: [1,0,2,1]
# Explanation: 215 + 806 = 1021
# 
# 
# 
# Example 4:
# 
# 
# Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
# Output: [1,0,0,0,0,0,0,0,0,0,0]
# Explanation: 9999999999 + 1 = 10000000000
# 
# 
# 
# 
# Note：
# 
# 
# 1 <= A.length <= 10000
# 0 <= A[i] <= 9
# 0 <= K <= 10000
# If A.length > 1, then A[0] != 0
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        # Schoolbook Addition
        # Time  complexity: O(max(N, logK))
        # Space complexity: O(max(N, logK))
        A[-1] += K
        for i in range(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i:
                A[i - 1] += carry

        if carry:
            A = list(map(int, str(carry))) + A

        return A
        
# @lc code=end

