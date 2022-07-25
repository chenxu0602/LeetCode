#
# @lc app=leetcode id=2333 lang=python3
#
# [2333] Minimum Sum of Squared Difference
#

# @lc code=start
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:

        # O(n)

        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        m = max(diff)
        n = len(nums1)
        bucket = [0] * (m + 1)

        for i in range(n):
            bucket[diff[i]] += 1

        k = k1 + k2
        for i in range(m, 0, -1):
            if bucket[i] > 0:
                remain = min(bucket[i], k)
                bucket[i] -= remain
                bucket[i - 1] += remain 
                k -= remain

        ans = 0
        for i in range(m, 0, -1):
            ans += bucket[i] * i * i

        return ans
        
# @lc code=end

