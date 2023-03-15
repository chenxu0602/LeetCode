#
# @lc app=leetcode id=2487 lang=python3
#
# [2487] Remove Nodes From Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        if not head: return head
        head.next = self.removeNodes(head.next)
        if head.next and head.val < head.next.val:
            return head.next
        return head
        """

        dummy = ListNode(float("inf"))
        stack = [dummy]

        while head:
            while stack and head.val > stack[-1].val:
                stack.pop()
            
            stack[-1].next = head
            stack.append(head)
            head = head.next

        return dummy.next
        
# @lc code=end

