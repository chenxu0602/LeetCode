#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (41.03%)
# Likes:    1994
# Dislikes: 503
# Total Accepted:    484.2K
# Total Submissions: 1.2M
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given the below binary tree and sum = 22,
# 
# 
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \      \
# 7    2      1
# 
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
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
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # Recursion
        # Time  complexity: O(N)
        # Space complexity: O(logN)
        # if not root:
        #     return False

        # sum -= root.val
        # if not root.left and not root.right:
        #     return sum == 0
        # return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

        # Iterations
        # Time  complexity: O(N)
        # Space complexity: O(logN)
        if not root:
            return False

        queue = [(root, sum - root.val),]
        while queue:
            node, curr_sum = queue.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                queue.append((node.right, curr_sum - node.right.val))
            if node.left:
                queue.append((node.left, curr_sum - node.left.val))
        return False

        
# @lc code=end

