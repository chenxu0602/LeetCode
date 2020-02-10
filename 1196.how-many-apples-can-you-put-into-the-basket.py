#
# @lc app=leetcode id=1196 lang=python3
#
# [1196] How Many Apples Can You Put into the Basket
#
# https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/description/
#
# algorithms
# Easy (67.75%)
# Likes:    33
# Dislikes: 8
# Total Accepted:    5.6K
# Total Submissions: 8.2K
# Testcase Example:  '[100,200,150,1000]'
#
# You have some apples, where arr[i] is the weight of the i-th apple.  You also
# have a basket that can carry up to 5000 units of weight.
# 
# Return the maximum number of apples you can put in the basket.
# 
# 
# Example 1:
# 
# 
# Input: arr = [100,200,150,1000]
# Output: 4
# Explanation: All 4 apples can be carried by the basket since their sum of
# weights is 1450.
# 
# 
# Example 2:
# 
# 
# Input: arr = [900,950,800,1000,700,800]
# Output: 5
# Explanation: The sum of weights of the 6 apples exceeds 5000 so we choose any
# 5 of them.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^3
# 1 <= arr[i] <= 10^3
# 
# 
#

# @lc code=start
class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        
# @lc code=end

