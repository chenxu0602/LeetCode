#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#
# https://leetcode.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (50.87%)
# Likes:    1227
# Dislikes: 131
# Total Accepted:    183.3K
# Total Submissions: 359.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Find the sum of all left leaves in a given binary tree.
# 
# Example:
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# There are two left leaves in the binary tree, with values 9 and 15
# respectively. Return 24.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # Iterative Tree Traversal (Pre-order)
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # if root is None: return 0

        # def is_leaf(node):
        #     return node is not None and node.left is None and node.right is None

        # stack, total = [root,], 0
        # while stack:
        #     sub_root = stack.pop()
        #     if is_leaf(sub_root.left):
        #         total += sub_root.left.val
        #     if sub_root.right is not None:
        #         stack.append(sub_root.right)
        #     if sub_root.left is not None:
        #         stack.append(sub_root.left)

        # return total


        # Recursive Tree Traversal (Pre-order)
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # def process_subtree(subtree, is_left):
        #     if subtree is None: return 0

        #     if subtree.left is None and subtree.right is None:
        #         return subtree.val if is_left else 0

        #     return process_subtree(subtree.left, True) + process_subtree(subtree.right, False)

        # return process_subtree(root, False)


        # return 0 if not root else (root.left.val if root.left and not (root.left.left or root.left.right) else 0) + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


        stack, tot, isLeft = [], 0, False

        while stack or root:
            if root:
                stack.append(root)

                if isLeft and not (root.left or root.right):
                    tot += root.val

                root, isLeft = root.left, True
            else:
                root, isLeft = stack.pop().right, False

        return tot
            
        
        
# @lc code=end

