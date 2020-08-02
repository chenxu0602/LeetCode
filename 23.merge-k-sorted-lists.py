#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (37.98%)
# Likes:    3670
# Dislikes: 234
# Total Accepted:    541.7K
# Total Submissions: 1.4M
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

import heapq

class ListNodeExtension(ListNode):
    def __lt__(self, x):
        return self.val < x.val

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        ListNode.__lt__ = ListNodeExtension.__lt__

        dummy = head = ListNode(0)
        heap = [(node.val, node) for node in lists if node]
        heapq.heapify(heap)

        while heap:
            val, node = heapq.heappop(heap)
            head.next = node
            head = head.next 
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, node))

        return dummy.next 
        
# @lc code=end

