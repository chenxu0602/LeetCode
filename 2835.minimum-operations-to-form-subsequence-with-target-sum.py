#
# @lc app=leetcode id=2835 lang=python3
#
# [2835] Minimum Operations to Form Subsequence With Target Sum
#

# @lc code=start
import heapq

class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:

        sm, ans = sum(nums), 0
        if sm < target: return -1

        nums = list(map(lambda x: -x, nums))
        heapq.heapify(nums)

        while target:
            num = -heapq.heappop(nums)
            sm -= num

            if sm < target < num:
                ans += 1
                sm  += num

                heapq.heappush(nums, -num // 2)
                heapq.heappush(nums, -num // 2)

            target -= num * (num <= target)

        return ans
        
# @lc code=end

