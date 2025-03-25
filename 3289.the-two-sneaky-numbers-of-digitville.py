#
# @lc app=leetcode id=3289 lang=python3
#
# [3289] The Two Sneaky Numbers of Digitville
#

# @lc code=start
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        s, ans = set(), []

        for num in nums:
            if num in s:
                ans += num,
            else:
                s.add(num)

        return ans


        
# @lc code=end

