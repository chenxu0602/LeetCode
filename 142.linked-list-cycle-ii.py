#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#
# https://leetcode.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (37.08%)
# Likes:    2825
# Dislikes: 224
# Total Accepted:    332.2K
# Total Submissions: 893.1K
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.
# 
# To represent a cycle in the given linked list, we use an integer pos which
# represents the position (0-indexed) in the linked list where tail connects
# to. If pos is -1, then there is no cycle in the linked list.
# 
# Note: Do not modify the linked list.
# 
# 
# 
# Example 1:
# 
# 
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the
# second node.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the
# first node.
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
# 
# 
# 
# 
# 
# 
# Follow-up:
# Can you solve it without using extra space?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        # Hash Table
        # Time  complexity: O(n)
        # Space complexity: O(n)
        # visited, node = set(), head
        # while node is not None:
        #     if node in visited:
        #         return node
        #     else:
        #         visited.add(node)
        #         node = node.next
        # return None
        

        # Floyd's Tortoise and Hare
        # Time  complexity: O(n)
        # Space complexity: O(1)
        if head is None or head.next is None:
            return None

        slow = fast = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break

        if slow == fast:
            slow = head
            while slow is not fast:
                slow, fast = slow.next, fast.next

            return slow

        return None
        
# @lc code=end

