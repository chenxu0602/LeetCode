#
# @lc app=leetcode id=1385 lang=python3
#
# [1385] Find the Distance Value Between Two Arrays
#
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/
#
# algorithms
# Easy (66.59%)
# Likes:    131
# Dislikes: 531
# Total Accepted:    21K
# Total Submissions: 31.6K
# Testcase Example:  '[4,5,8]\n[10,9,1,8]\n2'
#
# Given two integer arrays arr1 and arr2, and the integer d, return the
# distance value between the two arrays.
# 
# The distance value is defined as the number of elements arr1[i] such that
# there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
# 
# 
# Example 1:
# 
# 
# Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
# Output: 2
# Explanation: 
# For arr1[0]=4 we have: 
# |4-10|=6 > d=2 
# |4-9|=5 > d=2 
# |4-1|=3 > d=2 
# |4-8|=4 > d=2 
# For arr1[1]=5 we have: 
# |5-10|=5 > d=2 
# |5-9|=4 > d=2 
# |5-1|=4 > d=2 
# |5-8|=3 > d=2
# For arr1[2]=8 we have:
# |8-10|=2 <= d=2
# |8-9|=1 <= d=2
# |8-1|=7 > d=2
# |8-8|=0 <= d=2
# 
# 
# Example 2:
# 
# 
# Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr1.length, arr2.length <= 500
# -10^3 <= arr1[i], arr2[j] <= 10^3
# 0 <= d <= 100
# 
# 
#

# @lc code=start
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # return sum(all(abs(a - b) > d for b in arr2) for a in arr1)


        def is_valid(val):
            l, r = 0, len(arr2)
            while l < r:
                mid = (l + r) // 2
                if abs(arr2[mid] - val) <= d:
                    return False
                elif arr2[mid] > val:
                    r = mid
                else:
                    l = mid + 1

            return True

        arr2.sort()
        return sum(is_valid(x) for x in arr1)
        
# @lc code=end

