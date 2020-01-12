#
# @lc app=leetcode id=248 lang=python3
#
# [248] Strobogrammatic Number III
#
# https://leetcode.com/problems/strobogrammatic-number-iii/description/
#
# algorithms
# Hard (37.17%)
# Likes:    134
# Dislikes: 120
# Total Accepted:    22.7K
# Total Submissions: 60.2K
# Testcase Example:  '"50"\n"100"'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
# 
# Write a function to count the total strobogrammatic numbers that exist in the
# range of low <= num <= high.
# 
# Example:
# 
# 
# Input: low = "50", high = "100"
# Output: 3 
# Explanation: 69, 88, and 96 are three strobogrammatic numbers.
# 
# Note:
# Because the range might be a large number, the low and high numbers are
# represented as string.
# 
#

# @lc code=start
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:

        all_strobo = []
        for length in range(len(low), len(high)+1):
            all_strobo += self.strobo(length)
        res = 0
        for num in all_strobo:
            if int(low) <= int(num) <= int(high):
                res += 1
        return res

    def strobo(self, n):
        res = [""]

        if n % 2 == 1:
            res = list("018")

        while n > 1:
            n -= 2
            res = [a + num + b for a, b in "00 11 88 69 96".split()[n<2:] for num in res]
        return res

    """
    def strobo(self, n):
        self.mapping = {"0": "0", "1": "1", "6": "9", "9": "6", "8": "8"}
        self.res = []
        if n % 2:
            for i in ['0', '1', '8']:
                self.dfs(str(i), n-1)
        else:
            self.dfs("", n)
        return self.res

    def dfs(self, num, n):
        if n == 0:
            self.res.append(num)
            return

        for number in self.mapping:
            if n < 2 and number != "0":
                self.dfs(number + num + self.mapping[number], n-2)
            elif n >= 2:
                self.dfs(number + num + self.mapping[number], n-2)
    """
        
# @lc code=end

