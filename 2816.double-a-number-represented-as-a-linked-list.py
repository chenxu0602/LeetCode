#
# @lc app=leetcode id=2816 lang=python3
#
# [2816] Double a Number Represented as a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def dfs(node):
            sm = 2 * node.val + (dfs(node.next) if node.next else 0)
            carry, node.val = divmod(sm, 10)
            return carry

        return ListNode(1, head) if dfs(head) else head
        
# @lc code=end

