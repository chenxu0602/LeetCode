#
# @lc app=leetcode id=919 lang=python3
#
# [919] Complete Binary Tree Inserter
#
# https://leetcode.com/problems/complete-binary-tree-inserter/description/
#
# algorithms
# Medium (55.68%)
# Likes:    181
# Dislikes: 40
# Total Accepted:    10.9K
# Total Submissions: 19.6K
# Testcase Example:  '["CBTInserter","insert","get_root"]\n[[[1]],[2],[]]'
#
# A complete binary tree is a binary tree in which every level, except possibly
# the last, is completely filled, and all nodes are as far left as possible.
# 
# Write a data structure CBTInserter that is initialized with a complete binary
# tree and supports the following operations:
# 
# 
# CBTInserter(TreeNode root) initializes the data structure on a given tree
# with head node root;
# CBTInserter.insert(int v) will insert a TreeNode into the tree with value
# node.val = v so that the tree remains complete, and returns the value of the
# parent of the inserted TreeNode;
# CBTInserter.get_root() will return the head node of the tree.
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
# Output: [null,1,[1,2]]
# 
# 
# 
# Example 2:
# 
# 
# Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs =
# [[[1,2,3,4,5,6]],[7],[8],[]]
# Output: [null,3,4,[1,2,3,4,5,6,7,8]]
# 
# 
# 
# 
# 
# Note:
# 
# 
# The initial given tree is complete and contains between 1 and 1000 nodes.
# CBTInserter.insert is called at most 10000 times per test case.
# Every value of a given or inserted node is between 0 and 5000.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.queue = deque()
        self.root = root
        q = deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.queue.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        

    def insert(self, v: int) -> int:
        node = self.queue[0]
        self.queue.append(TreeNode(v))
        if not node.left:
            node.left = self.queue[-1]
        else:
            node.right = self.queue[-1]
            self.queue.popleft()
        return node.val
        

    def get_root(self) -> TreeNode:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()

