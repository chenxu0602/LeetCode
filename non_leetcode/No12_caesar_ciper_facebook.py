#!/usr/bin/python
# coding=utf-8
################################################################################
'''
https://leetcode.com/discuss/interview-question/395045/Facebook-or-Phone-Screen-or-Caesar-Cipher

Question 1:
Caesar Cipher Encrpytion
You are given a list of string, group them if they are same after using
Ceaser Cipher Encrpytion.
Definition of "same", "abc" can right shift 1, get "bcd",
here you can shift as many time as you want, the string will be considered as same.

Example:

Input: ["abc", "bcd", "acd", "dfg"]
Output: [["abc", "bcd"], ["acd", "dfg"]]
'''
################################################################################
from collections import defaultdict
class Solution(object):
    def caesar_cipher(self, array):

        array_dict = defaultdict(list)
        for item in array:
            current = []
            for i in range(len(item)):
                diff = ord(item[i]) - ord(item[0])
                diff = (diff + 26) % 26
                current.append(diff)
            array_dict[tuple(current)].append(item)

        res = []
        for key, values in array_dict.iteritems():
            res.append(values[:])
        return res


a = Solution()
a.caesar_cipher(["abc", "bcd", "acd", "dfg"])
