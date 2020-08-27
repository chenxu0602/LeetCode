#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#
# https://leetcode.com/problems/maximum-width-of-binary-tree/description/
#
# algorithms
# Medium (39.55%)
# Likes:    916
# Dislikes: 203
# Total Accepted:    48.1K
# Total Submissions: 121.5K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# Given a binary tree, write a function to get the maximum width of the given
# tree. The width of a tree is the maximum width among all levels. The binary
# tree has the same structure as a full binary tree, but some nodes are null.
# 
# The width of one level is defined as the length between the end-nodes (the
# leftmost and right most non-null nodes in the level, where the null nodes
# between the end-nodes are also counted into the length calculation.
# 
# Example 1:
# 
# 
# Input: 
# 
# ⁠          1
# ⁠        /   \
# ⁠       3     2
# ⁠      / \     \  
# ⁠     5   3     9 
# 
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4
# (5,3,null,9).
# 
# 
# Example 2:
# 
# 
# Input: 
# 
# ⁠         1
# ⁠        /  
# ⁠       3    
# ⁠      / \       
# ⁠     5   3     
# 
# Output: 2
# Explanation: The maximum width existing in the third level with the length 2
# (5,3).
# 
# 
# Example 3:
# 
# 
# Input: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2 
# ⁠      /        
# ⁠     5      
# 
# Output: 2
# Explanation: The maximum width existing in the second level with the length 2
# (3,2).
# 
# 
# Example 4:
# 
# 
# Input: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      /     \  
# ⁠     5       9 
# ⁠    /         \
# ⁠   6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8
# (6,null,null,null,null,null,null,7).
# 
# 
# 
# 
# Note: Answer will in the range of 32-bit signed integer.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # BFS Traversal
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # if not root: return 0

        # max_width = 0
        # queue = deque([(root, 0)])

        # while queue:
        #     level_length = len(queue)
        #     _, level_head_index = queue[0]

        #     for _ in range(level_length):
        #         node, col_index = queue.popleft()
        #         if node.left:
        #             queue.append((node.left, 2 * col_index))
        #         if node.right:
        #             queue.append((node.right, 2 * col_index + 1))

        #     max_width = max(max_width, col_index - level_head_index + 1)

        # return max_width


        # queue = [(root, 0, 0)]
        # cur_depth = left = ans = 0
        # for node, depth, pos in queue:
        #     if node:
        #         queue.append((node.left, depth + 1, pos * 2))
        #         queue.append((node.right, depth + 1, pos * 2 + 1))
        #         if cur_depth != depth:
        #             cur_depth = depth
        #             left = pos
        #         ans = max(pos - left + 1, ans)
        # return ans

        
        # BFS Traversal
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # table contains the first col_index for each level
        # first_col_index_table = {}
        # max_width = 0

        # def dfs(node, depth, col_index):
        #     nonlocal max_width
        #     if node is None: return
        #     # if the entry is empty, set the value
        #     if depth not in first_col_index_table:
        #         first_col_index_table[depth] = col_index

        #     max_width = max(max_width, col_index - first_col_index_table[depth] + 1)

        #     # Preorder DFS, with the priority on the left child
        #     dfs(node.left, depth + 1, 2 * col_index)
        #     dfs(node.right, depth + 1, 2 * col_index + 1)

        # dfs(root, 0, 0)
        # return max_width


        self.ans = 0
        left = {}

        def dfs(node, depth=0, pos=0):
            if node:
                left.setdefault(depth, pos)
                self.ans = max(self.ans, pos - left[depth] + 1)
                dfs(node.left, depth + 1, pos * 2)
                dfs(node.right, depth + 1, pos * 2 + 1)

        dfs(root)
        return self.ans

# @lc code=end

