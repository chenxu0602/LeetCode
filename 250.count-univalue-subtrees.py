#
# @lc app=leetcode id=250 lang=python3
#
# [250] Count Univalue Subtrees
#
# https://leetcode.com/problems/count-univalue-subtrees/description/
#
# algorithms
# Medium (49.72%)
# Likes:    346
# Dislikes: 79
# Total Accepted:    47.6K
# Total Submissions: 94.4K
# Testcase Example:  '[5,1,5,5,5,null,5]'
#
# Given a binary tree, count the number of uni-value subtrees.
# 
# A Uni-value subtree means all nodes of the subtree have the same value.
# 
# Example :
# 
# 
# Input:  root = [5,1,5,5,5,null,5]
# 
# ⁠             5
# ⁠            / \
# ⁠           1   5
# ⁠          / \   \
# ⁠         5   5   5
# 
# Output: 4
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:

        """
        def is_uni(node):
            if node.left is None and node.right is None:
                self.count += 1
                return True

            isuni = True
            if node.left is not None:
                isuni = is_uni(node.left) and isuni and node.left.val == node.val
            if node.right is not None:
                isuni = is_uni(node.right) and isuni and node.right.val == node.val

            self.count += isuni
            return isuni


        if root is None:
            return 0

        self.count = 0
        is_uni(root)
        return self.count
        """

        def is_valid_part(node, val):
            if node is None: return True

            if not all([is_valid_part(node.left, node.val),
                        is_valid_part(node.right, node.val)]):
                return False

            self.count += 1
            return node.val == val

        self.count = 0
        is_valid_part(root, 0)
        return self.count

        """
        def checkUni(node):
            if not node:
                return True
            left, right = checkUni(node.left), checkUni(node.right)
            if left and right and (not node.left or node.left.val == node.val) and \
                (not node.right or node.right.val == node.val):
                self.count += 1
                return True
            return False

        self.count = 0
        checkUni(root)
        return self.count
        """

        
# @lc code=end

