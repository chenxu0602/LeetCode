#
# @lc app=leetcode id=1130 lang=python3
#
# [1130] Minimum Cost Tree From Leaf Values
#
# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/description/
#
# algorithms
# Medium (65.95%)
# Likes:    1504
# Dislikes: 117
# Total Accepted:    40K
# Total Submissions: 59.6K
# Testcase Example:  '[6,2,4]'
#
# Given an array arr of positive integers, consider all binary trees such
# that:
# 
# 
# Each node has either 0 or 2 children;
# The values of arr correspond to the values of each leaf in an in-order
# traversal of the tree.  (Recall that a node is a leaf if and only if it has 0
# children.)
# The value of each non-leaf node is equal to the product of the largest leaf
# value in its left and right subtree respectively.
# 
# 
# Among all possible binary trees considered, return the smallest possible sum
# of the values of each non-leaf node.  It is guaranteed this sum fits into a
# 32-bit integer.
# 
# 
# Example 1:
# 
# 
# Input: arr = [6,2,4]
# Output: 32
# Explanation:
# There are two possible trees.  The first has non-leaf node sum 36, and the
# second has non-leaf node sum 32.
# 
# ⁠   24            24
# ⁠  /  \          /  \
# ⁠ 12   4        6    8
# ⁠/  \               / \
# 6    2             2   4
# 
# 
# 
# Constraints:
# 
# 
# 2 <= arr.length <= 40
# 1 <= arr[i] <= 15
# It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is
# less than 2^31).
# 
#

# @lc code=start
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # res = 0
        # while len(arr) > 1:
        #     min_idx = arr.index(min(arr))

        #     if 0 < min_idx < len(arr) - 1:
        #         res += min(arr[min_idx - 1], arr[min_idx + 1]) * arr[min_idx]
        #     else:
        #         res += arr[1 if min_idx == 0 else min_idx - 1] * arr[min_idx]

        #     arr.pop(min_idx)
        # return res

        # Time  complexity: O(N^2)
        # Space complexity: O(N)
        # res = 0
        # while len(arr) > 1:
        #     i = arr.index(min(arr))
        #     res += min(arr[i-1:i] + arr[i+1:i+2]) * arr.pop(i)
        # return res


        # Just find the next greater element in the array, on the left and one right.
        # Time  complexity: O(N)
        # Space complexity: O(N)
        res, n = 0, len(arr)
        stack = [float("inf")]
        for a in arr:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)

        while len(stack) > 2:
            res += stack.pop() * stack[-1]

        return res
        
# @lc code=end

