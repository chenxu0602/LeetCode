#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (37.21%)
# Likes:    1842
# Dislikes: 121
# Total Accepted:    243K
# Total Submissions: 651.3K
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

        # if not head: return None

        # left, right = head, head
        # stop = False

        # def recurseAndReverse(right, m, n):
        #     nonlocal left, stop
        #     if n == 1: return 

        #     right = right.next

        #     if m > 1:
        #         left = left.next

        #     recurseAndReverse(right, m - 1, n - 1)

        #     if left == right or right.next == left:
        #         stop = True

        #     if not stop:
        #         left.val, right.val = right.val, left.val

        #         left = left.next

        # recurseAndReverse(right, m, n)
        # return head

        if not head: return None
        cur, pre = head, None

        while m > 1:
            pre, cur = cur, cur.next
            m, n = m - 1, n - 1

        tail, con = cur, pre

        while n:
            cur.next, pre, cur = pre, cur, cur.next
            n -= 1

        if con:
            con.next = pre
        else:
            head = pre

        tail.next = cur

        return head


        
# @lc code=end

