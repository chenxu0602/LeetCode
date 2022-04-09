#
# @lc app=leetcode id=2179 lang=python3
#
# [2179] Count Good Triplets in an Array
#

# @lc code=start
from sortedcontainers import SortedList

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        pos = [0] * len(nums1)
        for idx, b in enumerate(nums2):
            pos[b] = idx

        pos_in_b, pre_a = SortedList([pos[nums1[0]]]), [0]
        for a in nums1[1:]:
            pos_in_b.add(pos[a])
            pre_a.append(pos_in_b.bisect_left(pos[a]))

        pos_in_b, suf_a = SortedList([pos[nums1[-1]]]), [0]
        for a in reversed(nums1[:len(nums1) - 1]):
            idx = pos_in_b.bisect(pos[a])
            suf_a.append(len(pos_in_b) - idx)
            pos_in_b.add(pos[a])

        suf_a.reverse()

        ans = 0
        for x, y in zip(pre_a, suf_a):
            ans += x * y
        return ans
        
        
# @lc code=end

