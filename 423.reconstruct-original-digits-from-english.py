#
# @lc app=leetcode id=423 lang=python3
#
# [423] Reconstruct Original Digits from English
#
# https://leetcode.com/problems/reconstruct-original-digits-from-english/description/
#
# algorithms
# Medium (45.68%)
# Likes:    122
# Dislikes: 434
# Total Accepted:    19.4K
# Total Submissions: 42.5K
# Testcase Example:  '"owoztneoer"'
#
# Given a non-empty string containing an out-of-order English representation of
# digits 0-9, output the digits in ascending order.
# 
# Note:
# 
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original
# digits. That means invalid inputs such as "abc" or "zerone" are not
# permitted.
# Input length is less than 50,000.
# 
# 
# 
# Example 1:
# 
# Input: "owoztneoer"
# 
# Output: "012"
# 
# 
# 
# Example 2:
# 
# Input: "fviefuro"
# 
# Output: "45"
# 
# 
#
from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        l, cnt, ret = [('zero','z'),('one','o'),('two','w'),('three','h'),('four','u'),('five','f'),('six','x'),('seven','s'),('eight','g'),('nine','i')], Counter(s), []
        for i in [0, 2, 4 , 6, 8, 1, 3, 5, 7, 9]:
            n = cnt[l[i][1]]
            for c in l[i][0]:
                cnt[c] -= n
            ret += [str(i)]*n

        return "".join(sorted(ret))

        

