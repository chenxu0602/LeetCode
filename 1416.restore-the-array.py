#
# @lc app=leetcode id=1416 lang=python3
#
# [1416] Restore The Array
#
# https://leetcode.com/problems/restore-the-array/description/
#
# algorithms
# Hard (36.18%)
# Likes:    184
# Dislikes: 5
# Total Accepted:    6.7K
# Total Submissions: 18.4K
# Testcase Example:  '"1000"\n10000'
#
# A program was supposed to print an array of integers. The program forgot to
# print whitespaces and the array is printed as a string of digits and all we
# know is that all integers in the array were in the range [1, k] and there are
# no leading zeros in the array.
# 
# Given the string s and the integer k. There can be multiple ways to restore
# the array.
# 
# Return the number of possible array that can be printed as a string s using
# the mentioned program.
# 
# The number of ways could be very large so return it modulo 10^9 + 7
# 
# 
# Example 1:
# 
# 
# Input: s = "1000", k = 10000
# Output: 1
# Explanation: The only possible array is [1000]
# 
# 
# Example 2:
# 
# 
# Input: s = "1000", k = 10
# Output: 0
# Explanation: There cannot be an array that was printed this way and has all
# integer >= 1 and <= 10.
# 
# 
# Example 3:
# 
# 
# Input: s = "1317", k = 2000
# Output: 8
# Explanation: Possible arrays are
# [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]
# 
# 
# Example 4:
# 
# 
# Input: s = "2020", k = 30
# Output: 1
# Explanation: The only possible array is [20,20]. [2020] is invalid because
# 2020 > 30. [2,020] is ivalid because 020 contains leading zeros.
# 
# 
# Example 5:
# 
# 
# Input: s = "1234567890", k = 90
# Output: 34
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5.
# s consists of only digits and doesn't contain leading zeros.
# 1 <= k <= 10^9.
# 
#

# @lc code=start
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        # dp[i] records the number of possible array that can be printed as a string s[i:]
        n = len(s)
        s = [*map(int, s)] + [float("inf")]
        dp = [0] * n + [1]
        for i in range(n - 1, -1, -1):
            num, j = s[i], i + 1
            while 1 <= num <= k and j < n + 1:
                dp[i] = (dp[i] + dp[j]) % (10**9 + 7)
                num = 10 * num + s[j]
                j += 1
        return dp[0]


        # dp[i] += sum(dp[j] for j in range(i+1, min(i+d+1, n)) if valid(s[i:j])
        # And we don't need to check all the j from i+1 to len(s). That will make problem be O(n^2). We just need to check j from i+1 to i+K where K is log10(k) which is garanteed to be less than 10 as k <= 10 ^ 9 so that time complexity would be O(Kn)
        # N, K, M = len(s), len(str(k)) + 1, 10**9 + 7

        # def valid(s):
        #     return s[0] != '0' and int(s) <= k

        # dp = [0] * K
        # for i in range(N - 1, -1, -1):
        #     dp[i % K] = i > N - K and valid(s[i:])
        #     dp[i % K] = (dp[i % K] + sum(dp[j % K] for j in range(i + 1, min(i + K + 1, N)) if valid(s[i:j]))) % M
        # return dp[0]
            
        
# @lc code=end

