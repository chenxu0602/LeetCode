#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (39.12%)
# Likes:    3343
# Dislikes: 367
# Total Accepted:    440.9K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# 
# Input: 1->2
# Output: false
# 
# Example 2:
# 
# 
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev = None
        while slow:
            next, slow.next = slow.next, prev
            prev, slow = slow, next

        while prev:
            if prev.val != head.val:
                return False
            prev, head = prev.next, head.next

        return True
        
# @lc code=end

