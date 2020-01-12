#
# @lc app=leetcode id=466 lang=python3
#
# [466] Count The Repetitions
#
# https://leetcode.com/problems/count-the-repetitions/description/
#
# algorithms
# Hard (27.36%)
# Likes:    109
# Dislikes: 83
# Total Accepted:    8.1K
# Total Submissions: 29.6K
# Testcase Example:  '"acb"\n4\n"ab"\n2'
#
# Define S = [s,n] as the string S which consists of n connected strings s. For
# example, ["abc", 3] ="abcabcabc". 
# On the other hand, we define that string s1 can be obtained from string s2 if
# we can remove some characters from s2 such that it becomes s1. For example,
# “abc”  can be obtained from “abdbec” based on our definition, but it can not
# be obtained from “acbbe”.
# You are given two non-empty strings s1 and s2 (each at most 100 characters
# long) and two integers 0 ≤ n1 ≤ 10^6 and 1 ≤ n2 ≤ 10^6. Now consider the
# strings S1 and S2, where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer
# M such that [S2,M] can be obtained from S1.
# 
# Example:
# 
# Input:
# s1="acb", n1=4
# s2="ab", n2=2
# 
# Return:
# 2
# 
# 
#

# @lc code=start
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:

        """
        index, repeat_count = 0, 0
        s1_size, s2_size = len(s1), len(s2)
        for i in range(n1):
            for j in range(s1_size):
                if s1[j] == s2[index]:
                    index += 1
                if index == s2_size:
                    index = 0
                    repeat_count += 1
        return repeat_count // n2
        """

        if n1 == 0: return 0

        indexr = [0] * (len(s2) + 1)
        countr = [0] * (len(s1) + 1)

        index, count = 0, 0
        for i in range(n1):
            for j in range(len(s1)):
                if s1[j] == s2[index]:
                    index += 1
                if index == len(s2):
                    index = 0
                    count += 1

            countr[i] = count
            indexr[i] = index

            for k in range(i):
                if indexr[k] == index:
                    prev_count = countr[k]
                    pattern_count = (countr[i] - countr[k]) * ((n1 - 1 - k) // (i - k))
                    remain_count = countr[k + (n1 - 1 - k) % (i - k)] - countr[k]
                    return (prev_count + pattern_count + remain_count) // n2

        return countr[n1 - 1] // n2
        
        
# @lc code=end

