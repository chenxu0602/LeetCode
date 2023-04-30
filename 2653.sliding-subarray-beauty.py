#
# @lc app=leetcode id=2653 lang=python3
#
# [2653] Sliding Subarray Beauty
#

# @lc code=start
from sortedcontainers import SortedList

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:

        """
        ans, vals = [], SortedList()
        for i, v in enumerate(nums):
            vals.add(v)
            if i >= k:
                vals.remove(nums[i - k])
            if i >= k - 1:
                ans.append(min(0, vals[x - 1]))

        return ans
        """

        counter, ans = [0] * 50, [0] * (len(nums) - k + 1)
        for i in range(len(nums)):
            if nums[i] < 0:
                counter[nums[i] + 50] += 1

            if i - k >= 0 and nums[i - k] < 0:
                counter[nums[i - k] + 50] -= 1

            if i >= k - 1:
                count = 0
                for j in range(50):
                    count += counter[j]
                    if count >= x:
                        ans[i - k + 1] = j - 50
                        break

        return ans
        
# @lc code=end

