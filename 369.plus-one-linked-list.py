#
# @lc app=leetcode id=369 lang=python3
#
# [369] Plus One Linked List
#
# https://leetcode.com/problems/plus-one-linked-list/description/
#
# algorithms
# Medium (58.16%)
# Likes:    458
# Dislikes: 30
# Total Accepted:    47K
# Total Submissions: 80.7K
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

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # sentinel head
        # Time  complexity: O(N)
        # Space complexity: O(1)
        # sentinel = ListNode(0)
        # sentinel.next = head
        # not_nine = sentinel

        # # find the rightmost not-nine digit
        # while head:
        #     if head.val != 9:
        #         not_nine = head
        #     head = head.next

        # # increase this rightmost not-nine digit by 1
        # not_nine.val += 1
        # not_nine = not_nine.next

        # # set all the following nines to zeros
        # while not_nine:
        #     not_nine.val = 0
        #     not_nine = not_nine.next

        # return sentinel if sentinel.val else sentinel.next



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
        
# @lc code=end

