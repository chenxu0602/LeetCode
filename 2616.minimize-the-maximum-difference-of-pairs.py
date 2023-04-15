#
# @lc app=leetcode id=2616 lang=python3
#
# [2616] Minimize the Maximum Difference of Pairs
#

# @lc code=start
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        # Greedy + Binary Search
        # Time  complexity: O(nlog(max(nums)) + nlogn)
        # Space complexity: O(logn)

        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            k, i = 0, 1
            while i < n:
                if nums[i] - nums[i - 1] <= mid:
                    k += 1
                    i += 1

                i += 1

            if k >= p:
                right = mid
            else:
                left = mid + 1

        return left
        
# @lc code=end

