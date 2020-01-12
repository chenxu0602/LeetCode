#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#
# https://leetcode.com/problems/binary-watch/description/
#
# algorithms
# Easy (45.34%)
# Likes:    376
# Dislikes: 634
# Total Accepted:    65K
# Total Submissions: 143K
# Testcase Example:  '0'
#
# A binary watch has 4 LEDs on the top which represent the hours (0-11), and
# the 6 LEDs on the bottom represent the minutes (0-59).
# Each LED represents a zero or one, with the least significant bit on the
# right.
# 
# For example, the above binary watch reads "3:25".
# 
# Given a non-negative integer n which represents the number of LEDs that are
# currently on, return all possible times the watch could represent.
# 
# Example:
# Input: n = 1Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04",
# "0:08", "0:16", "0:32"]
# 
# 
# Note:
# 
# The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid,
# it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero, for
# example "10:2" is not valid, it should be "10:02".
# 
# 
#
from itertools import combinations
from collections import defaultdict

class Solution:
    def generateHash(self, num):
        num_hash = defaultdict(list)
        while num >= 0:
            n = num
            count = 0

            while n > 0:
                count += (n & 1)
                n  >>= 1

            num_hash[count].append(num)

            num = num - 1

        return num_hash

    def readBinaryWatch(self, num: int) -> List[str]:
        
        """
        res = []
        for Hs in range(0, min(num, 4)+1):
            Ms = num - Hs
            if not 0 <= Ms <= 6:
                continue

            hcomb = combinations(range(4), Hs)
            mcomb = combinations(range(6), Ms)

            hcomb = tuple(map(lambda hs: 0 + sum(2**i for i in hs), hcomb))
            mcomb = tuple(map(lambda ms: 0 + sum(2**i for i in ms), mcomb))

            res += ["{}:{:02d}".format(h, m) for h in hcomb for m in mcomb if h < 12 and m < 60]

        return res
        """

        """
        up, down = 11, 59
        up_hash = self.generateHash(up)
        down_hash = self.generateHash(down)

        n = num
        result = []
        while n >= 0:
            rest = num - n
            hours = up_hash[n]
            minutes = down_hash[rest]

            for hour in hours:
                for minute in minutes:
                    result.append("%d:%.2d"%(hour, minute))
            
            n = n - 1

        return result
        """

        return [str(h) + ':' + '0'*(m<10) + str(m) for h in range(12) for m in range(60) if (bin(m) + bin(h)).count('1') == num]

