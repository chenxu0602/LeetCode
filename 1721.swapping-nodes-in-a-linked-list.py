#
# @lc app=leetcode id=1721 lang=python3
#
# [1721] Swapping Nodes in a Linked List
#
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/
#
# algorithms
# Medium (64.77%)
# Likes:    67
# Dislikes: 10
# Total Accepted:    7.6K
# Total Submissions: 11.7K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# You are given the head of a linked list, and an integer k.
# 
# Return the head of the linked list after swapping the values of the k^th node
# from the beginning and the k^th node from the end (the list is 1-indexed).
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]
# 
# 
# Example 3:
# 
# 
# Input: head = [1], k = 1
# Output: [1]
# 
# 
# Example 4:
# 
# 
# Input: head = [1,2], k = 1
# Output: [2,1]
# 
# 
# Example 5:
# 
# 
# Input: head = [1,2,3], k = 2
# Output: [1,2,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is n.
# 1 <= k <= n <= 10^5
# 0 <= Node.val <= 100
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        length = 0
        frontNode = endNode = ListNode(0)
        frontNode.next = endNode.next = head
        currentNode = head

        while currentNode:
            length += 1
            if endNode:
                endNode = endNode.next

            if length == k:
                frontNode = currentNode
                endNode = head

            currentNode = currentNode.next

        frontNode.val, endNode.val = endNode.val, frontNode.val

        return head
        
# @lc code=end

