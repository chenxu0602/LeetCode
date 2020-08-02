#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (44.05%)
# Likes:    1325
# Dislikes: 44
# Total Accepted:    290.6K
# Total Submissions: 658.1K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
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
# ⁠/  \    / \
# 7    2  5   1
# 
# 
# Return:
# 
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
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
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        # Time  complexity: O(N^2)
        # Space complexity: O(N)

        if not root: return []

        if not root.left and not root.right and sum == root.val:
            return [[root.val]]

        return [[root.val] + i for i in self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)]

        # def dfs(node, sum_, l, res):
        #     if node.left is node.right and sum_ == node.val:
        #         l.append(node.val)
        #         res.append(l)
        #     if node.left:
        #         dfs(node.left, sum_-node.val, l+[node.val], res)
        #     if node.right:
        #         dfs(node.right, sum_-node.val, l+[node.val], res)

        # if not root: return []
        # res = []
        # dfs(root, sum, [], res)
        # return res

        # if not root: return []
        # res = []
        # stack = [(root, [root.val])]
        # while stack:
        #     curr, path = stack.pop()
        #     if curr.left is curr.right and sum(path) == sum_:
        #         res.append(path)

        #     if curr.right:
        #         stack.append((curr.right, path + [curr.right.val]))

        #     if curr.left:
        #         stack.append((curr.left, path + [curr.left.val]))

        # return res
        
# @lc code=end

