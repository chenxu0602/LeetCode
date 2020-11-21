#
# @lc app=leetcode id=1474 lang=python3
#
# [1474] Delete N Nodes After M Nodes of a Linked List
#
# https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/description/
#
# algorithms
# Easy (74.62%)
# Likes:    123
# Dislikes: 2
# Total Accepted:    6.5K
# Total Submissions: 8.7K
# Testcase Example:  '[1,2,3,4,5,6,7,8,9,10,11,12,13]\n2\n3'
#
# Given the head of a linked list and two integers m and n. Traverse the linked
# list and remove some nodes in the following way:
# 
# 
# Start with the head as the current node.
# Keep the first m nodes starting with the current node.
# Remove the next n nodes
# Keep repeating steps 2 and 3 until you reach the end of the list.
# 
# 
# Return the head of the modified list after removing the mentioned nodes.
# 
# Follow up question: How can you solve this problem by modifying the list
# in-place?
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3
# Output: [1,2,6,7,11,12]
# Explanation: Keep the first (m = 2) nodes starting from the head of the
# linked List  (1 ->2) show in black nodes.
# Delete the next (n = 3) nodes (3 -> 4 -> 5) show in read nodes.
# Continue with the same procedure until reaching the tail of the Linked List.
# Head of linked list after removing nodes is returned.
# 
# Example 2:
# 
# 
# 
# 
# Input: head = [1,2,3,4,5,6,7,8,9,10,11], m = 1, n = 3
# Output: [1,5,9]
# Explanation: Head of linked list after removing nodes is returned.
# 
# Example 3:
# 
# 
# Input: head = [1,2,3,4,5,6,7,8,9,10,11], m = 3, n = 1
# Output: [1,2,3,5,6,7,9,10,11]
# 
# 
# Example 4:
# 
# 
# Input: head = [9,3,7,7,9,10,8,2], m = 1, n = 2
# Output: [9,7,8]
# 
# 
# 
# Constraints:
# 
# 
# The given linked list will contain between 1 and 10^4 nodes.
# The value of each node in the linked list will be in the range [1, 10^6].
# 1 <= m,n <= 1000
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        i = 0
        while head:
            if i < m - 1:
                i += 1
            else:
                j = 0
                while j < n and head.next:
                    head.next = head.next.next
                    j += 1
                i = 0
            head = head.next
        return dummy.next
        
# @lc code=end

