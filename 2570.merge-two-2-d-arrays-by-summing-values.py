#
# @lc app=leetcode id=2570 lang=python3
#
# [2570] Merge Two 2D Arrays by Summing Values
#

# @lc code=start
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        n1, n2 = map(len, (nums1, nums2))
        i = j = 0
        res = []
        while i < n1 or j < n2:
            id = min(nums1[i][0] if i < n1 else float("inf"), nums2[j][0] if j < n2 else float("inf"))
            res.append([id, 0])

            if i < n1 and nums1[i][0] == id:
                res[-1][1] += nums1[i][1]
                i += 1

            if j < n2 and nums2[j][0] == id:
                res[-1][1] += nums2[j][1]
                j += 1

        return res

        
# @lc code=end

