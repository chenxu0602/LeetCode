#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (41.82%)
# Likes:    2322
# Dislikes: 358
# Total Accepted:    274.2K
# Total Submissions: 654.2K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
# 
# 
# 
# 
# Example:
# 
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5
# 
# Note:
# 
# 
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
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
    def reverseLinkedList(self, head, k):
        new_head, ptr = None, head
        while k:
            next_node = ptr.next
            ptr.next = new_head
            new_head = ptr
            ptr = next_node
            k -= 1
        return new_head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # count, ptr = 0, head

        # while count < k and ptr:
        #     ptr = ptr.next
        #     count += 1

        # if count == k:
        #     reversedHead = self.reverseLinkedList(head, k)
        #     head.next = self.reverseKGroup(ptr, k)
        #     return reversedHead

        # return head 

        ptr, ktail, new_head = head, None, None

        while ptr:
            count, ptr = 0, head

            while count < k and ptr:
                ptr = ptr.next
                count += 1

            if count == k:
                revHead = self.reverseLinkedList(head, k)

                if not new_head:
                    new_head = revHead

                if ktail:
                    ktail.next = revHead

                ktail, head = head, ptr

        if ktail:
            ktail.next = head

        return new_head if new_head else head

        
# @lc code=end

