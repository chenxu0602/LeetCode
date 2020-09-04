#
# @lc app=leetcode id=738 lang=python3
#
# [738] Monotone Increasing Digits
#
# https://leetcode.com/problems/monotone-increasing-digits/description/
#
# algorithms
# Medium (44.19%)
# Likes:    461
# Dislikes: 62
# Total Accepted:    22.6K
# Total Submissions: 50.9K
# Testcase Example:  '10'
#
# 
# Given a non-negative integer N, find the largest number that is less than or
# equal to N with monotone increasing digits.
# 
# (Recall that an integer has monotone increasing digits if and only if each
# pair of adjacent digits x and y satisfy x .)
# 
# 
# Example 1:
# 
# Input: N = 10
# Output: 9
# 
# 
# 
# Example 2:
# 
# Input: N = 1234
# Output: 1234
# 
# 
# 
# Example 3:
# 
# Input: N = 332
# Output: 299
# 
# 
# 
# Note:
# N is an integer in the range [0, 10^9].
# 
#

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        # Greedy
        # Time  complexity: O(D^2), where D = logN is the number of digits in N.
        # Space compleixty: O(D)
        digits = []
        A = list(map(int, str(N)))
        for i in range(len(A)):
            for d in range(1, 10):
                if digits + [d] * (len(A) - i) > A:
                    digits.append(d - 1)
                    break
            else:
                digits.append(9)

        return int("".join(map(str, digits)))


        # Truncate After Cliff
        # Time  complexity: O(D^2), where D = logN is the number of digits in N.
        # Space compleixty: O(D)
        # S = list(str(N))
        # i = 1
        # while i < len(S) and S[i - 1] <= S[i]:
        #     i += 1
        # while 0 < i < len(S) and S[i - 1] > S[i]:
        #     S[i - 1] = str(int(S[i - 1]) - 1)
        #     i -= 1

        # S[i + 1:] = '9' * (len(S) - i - 1)
        # return int(''.join(S))
        
# @lc code=end

