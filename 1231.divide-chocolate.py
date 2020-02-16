#
# @lc app=leetcode id=1231 lang=python3
#
# [1231] Divide Chocolate
#
# https://leetcode.com/problems/divide-chocolate/description/
#
# algorithms
# Hard (51.40%)
# Likes:    147
# Dislikes: 10
# Total Accepted:    6.2K
# Total Submissions: 12.1K
# Testcase Example:  '[1,2,3,4,5,6,7,8,9]\n5'
#
# You have one chocolate bar that consists of some chunks. Each chunk has its
# own sweetness given by the array sweetness.
# 
# You want to share the chocolate with your K friends so you start cutting the
# chocolate bar into K+1 pieces using K cuts, each piece consists of some
# consecutive chunks.
# 
# Being generous, you will eat the piece with the minimum total sweetness and
# give the other pieces to your friends.
# 
# Find the maximum total sweetness of the piece you can get by cutting the
# chocolate bar optimally.
# 
# 
# Example 1:
# 
# 
# Input: sweetness = [1,2,3,4,5,6,7,8,9], K = 5
# Output: 6
# Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8],
# [9]
# 
# 
# Example 2:
# 
# 
# Input: sweetness = [5,6,7,8,9,1,2,3,4], K = 8
# Output: 1
# Explanation: There is only one way to cut the bar into 9 pieces.
# 
# 
# Example 3:
# 
# 
# Input: sweetness = [1,2,2,1,2,2,1,2,2], K = 2
# Output: 5
# Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]
# 
# 
# 
# Constraints:
# 
# 
# 0 <= K < sweetness.length <= 10^4
# 1 <= sweetness[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:

        def divide(target):
            sum_, count = 0, 0
            for l in sweetness:
                sum_ += l
                if sum_ >= target:
                    count += 1
                    sum_ = 0
            return count

        lo, hi = min(sweetness), sum(sweetness) // (K + 1)
        while lo < hi:
            target = (lo + hi + 1) // 2
            if divide(target) < K + 1:
                hi = target - 1
            else:
                lo = target

        return lo
        
# @lc code=end

