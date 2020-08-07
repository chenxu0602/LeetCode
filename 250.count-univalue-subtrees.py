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

        # Depth First Search
        # Time  complexity: O(N)
        # Space complexity: O(H)
        # def uni_value(node):
        #     # base case - if the node has no children this is a univalue subtree
        #     if node.left is node.right:
        #         self.count += 1
        #         return True

        #     is_uni = True

        #     if node.left:
        #         is_uni = uni_value(node.left) and is_uni and node.left.val == node.val
        #     if node.right:
        #         is_uni = uni_value(node.right) and is_uni and node.right.val == node.val

        #     self.count += is_uni
        #     return is_uni

        # if not root: return 0
        # self.count = 0
        # uni_value(root)
        # return self.count




        # Depth First Search - Pass Parent Values
        # Time  complexity: O(N)
        # Space complexity: O(H)
        def is_valid_part(node, val):
            # considered a valid subtree
            if not node: return True

            # check if node.left and node.right are univalue subtrees of value node.val
            if not all([is_valid_part(node.left, node.val),
                        is_valid_part(node.right, node.val)]):
                return False

            self.count += 1

            return node.val == val

        self.count = 0
        is_valid_part(root, 0)
        return self.count



        # def checkUni(node):
        #     if not node: return True

        #     left, right = map(checkUni, (node.left, node.right))

        #     if left and right and (not node.left or node.left.val == node.val) and \
        #         (not node.right or node.right.val == node.val):
        #         self.count += 1
        #         return True

        #     return False

        # self.count = 0
        # checkUni(root)
        # return self.count
        
# @lc code=end

