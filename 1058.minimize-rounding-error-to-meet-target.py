#
# @lc app=leetcode id=1058 lang=python3
#
# [1058] Minimize Rounding Error to Meet Target
#
# https://leetcode.com/problems/minimize-rounding-error-to-meet-target/description/
#
# algorithms
# Medium (39.29%)
# Likes:    26
# Dislikes: 36
# Total Accepted:    1.4K
# Total Submissions: 3.4K
# Testcase Example:  '["0.700","2.800","4.900"]\n8'
#
# Given an array of prices [p1,p2...,pn] and a target, round each price pi to
# Roundi(pi) so that the rounded array [Round1(p1),Round2(p2)...,Roundn(pn)]
# sums to the given target. Each operation Roundi(pi) could be either Floor(pi)
# or Ceil(pi).
# 
# Return the string "-1" if the rounded array is impossible to sum to target.
# Otherwise, return the smallest rounding error, which is defined as Σ
# |Roundi(pi) - (pi)| for i from 1 to n, as a string with three places after
# the decimal.
# 
# 
# 
# Example 1:
# 
# 
# Input: prices = ["0.700","2.800","4.900"], target = 8
# Output: "1.000"
# Explanation: 
# Use Floor, Ceil and Ceil operations to get (0.7 - 0) + (3 - 2.8) + (5 - 4.9)
# = 0.7 + 0.2 + 0.1 = 1.0 .
# 
# 
# Example 2:
# 
# 
# Input: prices = ["1.500","2.500","3.500"], target = 10
# Output: "-1"
# Explanation: 
# It is impossible to meet the target.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= prices.length <= 500.
# Each string of prices prices[i] represents a real number which is between 0
# and 1000 and has exactly 3 decimal places.
# target is between 0 and 1000000.
# 
#
from math import floor, ceil
class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        maxV, minV, errors = 0, 0, []

        for p in prices:
            fp = float(p)
            f, c = floor(fp), ceil(fp)
            minV, maxV = minV + f, maxV + c
            errors.append((fp-f, c-fp))

        if target < minV or target > maxV:
            return "-1"

        ceilCount = target - minV

        errors = sorted(errors, reverse=True)

        minError = sum(e[1] for e in errors[:ceilCount]) + sum(e[0] for e in errors[ceilCount:])

        return "{:.3f}".format(minError)
        

