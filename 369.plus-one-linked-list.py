#
# @lc app=leetcode id=369 lang=python3
#
# [369] Plus One Linked List
#
# https://leetcode.com/problems/plus-one-linked-list/description/
#
# algorithms
# Medium (56.25%)
# Likes:    285
# Dislikes: 9
# Total Accepted:    34.5K
# Total Submissions: 61.2K
# Testcase Example:  '[1,2,3]'
#
# Given a non-negative integer represented as non-empty a singly linked list of
# digits, plus one to the integer.
# 
# You may assume the integer do not contain any leading zero, except the number
# 0 itself.
# 
# The digits are stored such that the most significant digit is at the head of
# the list.
# 
# 
# Example :
# 
# 
# Input: [1,2,3]
# Output: [1,2,4]
# 
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:


        """
        tail = None
        while head:
            head.next, head, tail = tail, head.next, head

        carry = 1
        while tail:
            carry, tail.val = divmod(carry + tail.val, 10)
            if carry and not tail.next:
                tail.next = ListNode(0)
            tail.next, tail, head = head, tail.next, tail

        return head
        """

        def dfs(node, carry):
            if not node:
                return carry

            node.val += dfs(node.next, carry)
            res, node.val = divmod(node.val, 10)
            return res

        res = dfs(head, 1)
        if res > 0:
            newHead = ListNode(res)
            newHead.next = head
            return newHead
        return head
        

