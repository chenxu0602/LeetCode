#
# @lc app=leetcode id=2181 lang=python3
#
# [2181] Merge Nodes in Between Zeros
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(float("-inf"))
        while head and head.next:
            prev.next = head
            head = head.next
            while head and head.val != 0:
                prev.next.val += head.val
                head = head.next
            prev = prev.next
        prev.next = None
        return dummy.next
        
# @lc code=end

