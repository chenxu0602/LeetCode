#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (35.73%)
# Likes:    1515
# Dislikes: 105
# Total Accepted:    219.9K
# Total Submissions: 605.9K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        """
        if not head:
            return None

        left, right = head, head
        stop = False

        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            if n == 1:
                return 

            right = right.next

            if m > 1:
                left = left.next

            recurseAndReverse(right, m-1, n-1)

            if left == right or right.next == left:
                stop = True

            if not stop:
                left.val, right.val = right.val, left.val
                left = left.next

        recurseAndReverse(right, m, n)
        return head
        """

        if not head:
            return None

        curr, prev = head, None
        while m > 1:
            prev = curr
            curr = curr.next
            m, n = m - 1, n - 1

        tail, con = curr, prev

        while n:
            third = curr.next
            curr.next = prev
            prev = curr
            curr = third
            n -= 1

        if con:
            con.next = prev
        else:
            head = prev

        tail.next = curr

        return head

        
# @lc code=end

