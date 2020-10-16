#
# @lc app=leetcode id=1088 lang=python3
#
# [1088] Confusing Number II
#
# https://leetcode.com/problems/confusing-number-ii/description/
#
# algorithms
# Hard (43.74%)
# Likes:    206
# Dislikes: 64
# Total Accepted:    16.1K
# Total Submissions: 36K
# Testcase Example:  '20'
#
# We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9
# are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3,
# 4, 5 and 7 are rotated 180 degrees, they become invalid.
# 
# A confusing number is a number that when rotated 180 degrees becomes a
# different number with each digit valid.(Note that the rotated number can be
# greater than the original number.)
# 
# Given a positive integer N, return the number of confusing numbers between 1
# and N inclusive.
# 
# 
# 
# Example 1:
# 
# 
# Input: 20
# Output: 6
# Explanation: 
# The confusing numbers are [6,9,10,16,18,19].
# 6 converts to 9.
# 9 converts to 6.
# 10 converts to 01 which is just 1.
# 16 converts to 91.
# 18 converts to 81.
# 19 converts to 61.
# 
# 
# Example 2:
# 
# 
# Input: 100
# Output: 19
# Explanation: 
# The confusing numbers are
# [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100].
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    count, n = 0, 0

    def confusingNumberII(self, N: int) -> int:
        nums = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        
        def find_total(n):
            if not n:
                return 1
            
            total = sum(n[0] > nn for nn in nums) * 5 ** (len(n) - 1)
            
            if n[0] in nums:
                total += find_total(n[1:])
                
            return total
        
        def find_strobogrammatic(arr, l, r):
            res = 0
            if l > r:
                n = "".join(arr)
                if int(n) < N:
                    res += 1
            else:
                for k, v in nums.items():
                    arr[l], arr[r] = k, v
                    if (len(arr) > 1 and arr[0] == '0') or (l == r and k != v):
                        continue
                    res += find_strobogrammatic(arr, l+1, r-1)
            return res
        
        n_str = str(N)
        total = find_total(n_str)
        for l in range(1, len(n_str)+1):
            total -= find_strobogrammatic([0] * l, 0, l - 1)
        return total    


        # def is_confusing(x):
        #     rot, orig = 0, x
        #     while x:
        #         x, r = divmod(x, 10)
        #         if r == 6:
        #             r = 9
        #         elif r == 9:
        #             r = 6
        #         rot = rot * 10 + r
        #     return True if rot != orig else False

        # def search(i):
        #     if i > self.n: return

        #     if i != 0:
        #         if is_confusing(i):
        #             self.count += 1
        #         search(i * 10)

        #     search(i * 10 + 1)
        #     search(i * 10 + 6)
        #     search(i * 10 + 8)
        #     search(i * 10 + 9)
            

        # self.n = N
        # search(0)
        # return self.count
        
# @lc code=end

