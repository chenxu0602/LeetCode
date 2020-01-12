#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (35.56%)
# Likes:    3064
# Dislikes: 203
# Total Accepted:    468.9K
# Total Submissions: 1.3M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
# Example:
# 
# 
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import heappush, heappop, heapreplace, heapify

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, x):
        return self.val == x.val

    def __lt__(self, x):
        return self.val < x.val

    def __gt__(self, x):
        return self.val > x.val

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = node = ListNode(0)
        h = [(n.val, n) for n in lists if n]
        heapify(h)

        while h:
            v, n = heappop(h)
            node.next = n
            node = node.next
            if n.next:
                heappush(h, (n.next.val, n.next))
        return dummy.next



        
# @lc code=end

