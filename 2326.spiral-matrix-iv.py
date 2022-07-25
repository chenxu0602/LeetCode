#
# @lc app=leetcode id=2326 lang=python3
#
# [2326] Spiral Matrix IV
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        num = m * n
        res = [[-1] * n for _ in range(m)]
        x, y = 0, 0
        dx, dy = 1, 0

        while head:
            res[y][x] = head.val
            if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= m or res[y + dy][x + dx] != -1:
                dx, dy = -dy, dx

            x, y = x + dx, y + dy
            head = head.next

        return res
        
# @lc code=end

