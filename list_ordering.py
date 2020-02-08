#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (31.85%)
# Likes:    1146
# Dislikes: 81
# Total Accepted:    177.2K
# Total Submissions: 541.3K
# Testcase Example:  '[1,2,3,4]'
#
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# Example 1:
# 
# 
# Given 1->2->3->4, reorder it to 1->4->2->3.
# 
# Example 2:
# 
# 
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def _splitList(head):
            fast = slow = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next
                fast = fast.next

            mid = slow.next
            slow.next = None
            return head, mid

        def _reverseList(head):
            last = None
            currentNode = head
            while currentNode:
                nextNode = currentNode.next
                currentNode.next = last
                last = currentNode
                currentNode = nextNode
            return last

        def _mergeLists(a, b):
            tail = a
            head = a

            a = a.next
            while b:
                tail.next = b
                tail = tail.next
                b = b.next
                if a:
                    a, b = b, a


        if not head or not head.next:
            return

        a, b = _splitList(head)
        b = _reverseList(b)
        head = _mergeLists(a, b)
        
# @lc code=end

