#
# @lc app=leetcode id=2779 lang=python3
#
# [2779] Maximum Beauty of an Array After Applying Operation
#

# @lc code=start
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:

        # nums.sort()
        # start, ans = 0, 0
        # for end in range(len(nums)):
        #     while nums[end] - nums[start] > 2 * k:
        #         start += 1

        #     ans = max(ans, end - start + 1)

        # return ans 


        cnt = [0] * (max(nums) + 2)
        for num in nums:
            cnt[max(0, num - k)] += 1
            cnt[min(len(cnt) - 1, num + k + 1)] -= 1

        res, curr = 0, 0
        for num in cnt:
            curr += num
            res = max(res, curr)

        return res 
    
        
# @lc code=end

