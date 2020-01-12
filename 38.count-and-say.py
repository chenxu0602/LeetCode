#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (41.39%)
# Likes:    918
# Dislikes: 7268
# Total Accepted:    322.4K
# Total Submissions: 767.8K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
# 
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# Given an integer n where 1 ≤ n ≤ 30, generate the n^th term of the
# count-and-say sequence.
# 
# Note: Each term of the sequence of integers will be represented as a
# string.
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "1"
# 
# 
# Example 2:
# 
# 
# Input: 4
# Output: "1211"
# 
#

# @lc code=start
from itertools import groupby
import re

class Solution:
    def countAndSay(self, n: int) -> str:
        """
        s = '1'
        for _ in range(n-1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s
        """

        """
        s = '1'
        for _ in range(n-1):
            s = "".join(str(len(group)) + digit for group, digit in re.findall(r'((.)\2*)', s))
        return s
        """

        s = '1'
        for _ in range(n-1):
            s = "".join(str(len(list(group))) + digit for digit, group in groupby(s))
        return s

        """
        if n == '1':
            return '1'
        else:
            return ''.join(str(len(x)) + x[0] for x in [list(g) for k, g in itertools.groupby(self.countAndSay(n-1))])
        """
        
# @lc code=end

