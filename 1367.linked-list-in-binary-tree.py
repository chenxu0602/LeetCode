#
# @lc app=leetcode id=1367 lang=python3
#
# [1367] Linked List in Binary Tree
#
# https://leetcode.com/problems/linked-list-in-binary-tree/description/
#
# algorithms
# Medium (41.15%)
# Likes:    589
# Dislikes: 22
# Total Accepted:    22.8K
# Total Submissions: 55.4K
# Testcase Example:  '[4,2,8]\n[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]'
#
# Given a binary tree root and a linked list with head as the first node. 
# 
# Return True if all the elements in the linked list starting from the head
# correspond to some downward path connected in the binary tree otherwise
# return False.
# 
# In this context downward path means a path that starts at some node and goes
# downwards.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: head = [4,2,8], root =
# [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true
# Explanation: Nodes in blue form a subpath in the binary Tree.  
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: head = [1,4,2,6], root =
# [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: head = [1,4,2,6,8], root =
# [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: false
# Explanation: There is no path in the binary tree that contains all the
# elements of the linked list from head.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= node.val <= 100 for each node in the linked list and binary tree.
# The given linked list will contain between 1 and 100 nodes.
# The given binary tree will contain between 1 and 2500 nodes.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:

        def dfs(head, root):
            if not head: return True
            if not root: return False
            return root.val == head.val and (dfs(head.next, root.left) or dfs(head.next, root.right))

        if not root: return False
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        
# @lc code=end

