#
# @lc app=leetcode id=655 lang=python3
#
# [655] Print Binary Tree
#
# https://leetcode.com/problems/print-binary-tree/description/
#
# algorithms
# Medium (52.25%)
# Likes:    238
# Dislikes: 584
# Total Accepted:    22.6K
# Total Submissions: 43.2K
# Testcase Example:  '[1,2]'
#
# Print a binary tree in an m*n 2D string array following these rules: 
# 
# 
# The row number m should be equal to the height of the given binary tree.
# The column number n should always be an odd number.
# The root node's value (in string format) should be put in the exactly middle
# of the first row it can be put. The column and the row where the root node
# belongs will separate the rest space into two parts (left-bottom part and
# right-bottom part). You should print the left subtree in the left-bottom part
# and print the right subtree in the right-bottom part. The left-bottom part
# and the right-bottom part should have the same size. Even if one subtree is
# none while the other is not, you don't need to print anything for the none
# subtree but still need to leave the space as large as that for the other
# subtree. However, if two subtrees are none, then you don't need to leave
# space for both of them. 
# Each unused space should contain an empty string "".
# Print the subtrees following the same rules.
# 
# 
# Example 1:
# 
# Input:
# ⁠    1
# ⁠   /
# ⁠  2
# Output:
# [["", "1", ""],
# ⁠["2", "", ""]]
# 
# 
# 
# 
# Example 2:
# 
# Input:
# ⁠    1
# ⁠   / \
# ⁠  2   3
# ⁠   \
# ⁠    4
# Output:
# [["", "", "", "1", "", "", ""],
# ⁠["", "2", "", "", "", "3", ""],
# ⁠["", "", "4", "", "", "", ""]]
# 
# 
# 
# Example 3:
# 
# Input:
# ⁠     1
# ⁠    / \
# ⁠   2   5
# ⁠  / 
# ⁠ 3 
# ⁠/ 
# 4 
# Output:
# 
# [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
# ⁠["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
# ⁠["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
# ⁠["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
# 
# 
# 
# Note:
# The height of binary tree is in the range of [1, 10].
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def getHeight(self, root):
        if not root: return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def fill(self, root, grid, row, left, right):
        if not root: return
        mid = (left + right) // 2
        grid[row][mid] = str(root.val)
        self.fill(root.left, grid, row+1, left, mid-1)
        self.fill(root.right, grid, row+1, mid+1, right)

    def printTree(self, root: TreeNode) -> List[List[str]]:
        
        height = self.getHeight(root)
        grid = [[""] * ((1 << height) - 1) for _ in range(height)]
        self.fill(root, grid, 0, 0, len(grid[0]) - 1)

        return grid

        
        

