#
# @lc app=leetcode id=817 lang=python3
#
# [817] Linked List Components
#
# https://leetcode.com/problems/linked-list-components/description/
#
# algorithms
# Medium (57.19%)
# Likes:    392
# Dislikes: 1065
# Total Accepted:    45.8K
# Total Submissions: 80K
# Testcase Example:  '[0,1,2,3]\n[0,1,3]'
#
# We are given head, the head node of a linked list containing unique integer
# values.
# 
# We are also given the list G, a subset of the values in the linked list.
# 
# Return the number of connected components in G, where two values are
# connected if they appear consecutively in the linked list.
# 
# Example 1:
# 
# 
# Input: 
# head: 0->1->2->3
# G = [0, 1, 3]
# Output: 2
# Explanation: 
# 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
# 
# 
# Example 2:
# 
# 
# Input: 
# head: 0->1->2->3->4
# G = [0, 3, 1, 4]
# Output: 2
# Explanation: 
# 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the
# two connected components.
# 
# 
# Note: 
# 
# 
# If N is the length of the linked list given by head, 1 <= N <= 10000.
# The value of each node in the linked list will be in the range [0, N -
# 1].
# 1 <= G.length <= 10000.
# G is a subset of all values in the linked list.
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
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        # Grouping
        # Time  complexity: O(N + G.length), where N is the length of the linked list with root node head.
        # Space compleixty: O(G.length)
        Gset = set(G)
        cur, ans = head, 0
        while cur:
            if cur.val in Gset and getattr(cur.next, 'val', None) not in Gset:
                ans += 1
            cur = cur.next

        return ans


        # count, cur = 0, head
        # while cur:
        #     if cur.val in G:
        #         count += 1
        #         while cur and cur.val in G:
        #             cur = cur.next
        #     else:
        #         cur = cur.next

        # return count
        
# @lc code=end

