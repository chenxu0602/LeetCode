#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (34.78%)
# Likes:    2604
# Dislikes: 190
# Total Accepted:    525.5K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, remove the n-th node from the end of list and return its
# head.
# 
# Example:
# 
# 
# Given linked list: 1->2->3->4->5, and n = 2.
# 
# After removing the second node from the end, the linked list becomes
# 1->2->3->5.
# 
# 
# Note:
# 
# Given n will always be valid.
# 
# Follow up:
# 
# Could you do this in one pass?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        # slow = fast = head
        # for _ in range(n):
        #     fast = fast.next

        # if not fast:
        #     return head.next

        # while fast.next:
        #     slow, fast = slow.next, fast.next

        # slow.next = slow.next.next

        # return head


        def remove(head):
            if not head:
                return 0, head

            i, head.next = remove(head.next)
            return i + 1, (head, head.next)[i + 1 == n]

        return remove(head)[1]
        
# @lc code=end

