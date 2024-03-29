#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (59.32%)
# Likes:    3500
# Dislikes: 78
# Total Accepted:    817.2K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # Recursive
        # Time  complexity: O(n)
        # Space complexity: O(n)
        # if not head or not head.next:
        #     return head
        
        # p = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None

        # return p

        

        # Iterative
        # Time  complexity: O(n)
        # Space complexity: O(1)
        """
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
        """

        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

        
        
# @lc code=end

