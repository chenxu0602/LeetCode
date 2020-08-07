#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (51.36%)
# Likes:    1635
# Dislikes: 87
# Total Accepted:    229.6K
# Total Submissions: 446.8K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
# 
# Example:
# 
# 
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
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
    def rightSideView(self, root: TreeNode) -> List[int]:

        # Recursive DFS
        # Time  complexity: O(N)
        # Space complexity: O(H)
        # if root is None:
        #     return []

        # rightside = []

        # def helper(node: TreeNode, level: int) -> None:
        #     if level == len(rightside):
        #         rightside.append(node.val)
        #     for child in [node.right, node.left]:
        #         if child:
        #             helper(child, level + 1)

        # helper(root, 0)
        # return rightside


        if not root: return []
        right, left = map(self.rightSideView, (root.right, root.left))
        return [root.val] + right + left[len(right):]

        
# @lc code=end

