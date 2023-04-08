#
# @lc app=leetcode id=2569 lang=python3
#
# [2569] Handling Sum Queries After Update
#

# @lc code=start
class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:

        x = sum(a << i for i, a in enumerate(nums1))
        cur = sum(nums2)
        res = []

        for i, j, k in queries:
            if i == 1:
                x ^= (1 << j) - 1
                x ^= (1 << k + 1) - 1
            elif i == 2:
                cur += j * x.bit_count()
            else:
                res.append(cur)

        return res
        
# @lc code=end

