#
# @lc app=leetcode id=2343 lang=python3
#
# [2343] Query Kth Smallest Trimmed Number
#

# @lc code=start
class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans, trimmed = [], {}
        for k, trim in queries:
            trimmed.setdefault(trim, sorted([(num[-trim:], i) for i, num in enumerate(nums)]))
            ans.append(trimmed[trim][k - 1][1])
        return ans
        
# @lc code=end

