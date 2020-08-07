#
# @lc app=leetcode id=255 lang=python3
#
# [255] Verify Preorder Sequence in Binary Search Tree
#
# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/description/
#
# algorithms
# Medium (45.61%)
# Likes:    602
# Dislikes: 51
# Total Accepted:    48.5K
# Total Submissions: 106.1K
# Testcase Example:  '[5,2,6,1,3]'
#
# Given an array of numbers, verify whether it is the correct preorder
# traversal sequence of a binary search tree.
# 
# You may assume each number in the sequence is unique.
# 
# Consider the following binary search tree: 
# 
# 
# ⁠    5
# ⁠   / \
# ⁠  2   6
# ⁠ / \
# ⁠1   3
# 
# Example 1:
# 
# 
# Input: [5,2,6,1,3]
# Output: false
# 
# Example 2:
# 
# 
# Input: [5,2,1,3,6]
# Output: true
# 
# Follow up:
# Could you do it using only constant space complexity?
# 
#

# @lc code=start
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:

        # stack, root = [], float("-inf")
        # for num in preorder:
        #     if num < root:
        #         return False

        #     while stack and num > stack[-1]:
        #         root = stack.pop()

        #     stack.append(num)

        # return True


        lower = float("-inf")
        i = 0
        for num in preorder:
            if num < lower:
                return False

            while i > 0 and num > preorder[i-1]:
                lower = preorder[i-1]
                i -= 1

            preorder[i] = num
            i += 1

        return True
        
# @lc code=end

