#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (39.52%)
# Likes:    1724
# Dislikes: 337
# Total Accepted:    235.9K
# Total Submissions: 595.4K
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
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        # dummy = jump = ListNode(0)
        # dummy.next = l = r = head

        # while True:
        #     count = 0
        #     while r and count < k:
        #         r = r.next
        #         count += 1
        #     if count == k:
        #         pre, cur = r, l
        #         for _ in range(k):
        #             cur.next, cur, pre = pre, cur.next, cur
        #         jump.next, jump, l = pre, l, r
        #     else:
        #         return dummy.next


        def reverse(head, count):
            pre, cur, nxt = None, head, head
            while count > 0:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
                count -= 1
            return cur, pre

        count, node = 0, head
        while node and count < k:
            node = node.next 
            count += 1

        if count < k: return head
        new_head, pre = reverse(head, count)
        head.next = self.reverseKGroup(new_head, k)
        return pre

# @lc code=end

