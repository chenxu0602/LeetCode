#
# @lc app=leetcode id=466 lang=python3
#
# [466] Count The Repetitions
#
# https://leetcode.com/problems/count-the-repetitions/description/
#
# algorithms
# Hard (27.85%)
# Likes:    146
# Dislikes: 117
# Total Accepted:    9.5K
# Total Submissions: 34K
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
        # Time  complexity: O(n1 * size(s1))
        # Space complexity: O(1)
        # index, repeat_count = 0, 0
        # s1_size, s2_size = map(len, (s1, s2))
        # for i in range(n1):
        #     for j in range(s1_size):
        #         if s1[j] == s2[index]:
        #             index += 1
        #         if index == s2_size:
        #             index = 0
        #             repeat_count += 1

        # return repeat_count // n2


        # According to the Pigeonhole principle, we need to iterate over s1 only (size(s2) + 1) times at max.
        # Time  complexity: O(size(s1) * size(s2))
        # Space complexity: O(size(s2))
        start = {}
        s1_round, s2_round, s2_idx = 0, 0, 0
        while s1_round < n1:
            s1_round += 1
            for ch in s1:
                if ch == s2[s2_idx]:
                    s2_idx += 1
                    if s2_idx == len(s2):
                        s2_round += 1
                        s2_idx = 0
                        
            if s2_idx in start:
                prev_s1_round, prev_s2_round = start[s2_idx]
                circle_s1_round = s1_round - prev_s1_round
                circle_s2_round = s2_round - prev_s2_round
                res = int((n1 - prev_s1_round) / circle_s1_round) * circle_s2_round
                left_s1_round = (n1 - prev_s1_round) % circle_s1_round + prev_s1_round
                for key, val in start.items():
                    if val[0] == left_s1_round:
                        res += val[1]
                        break
                return int(res / n2)
            else:
                start[s2_idx] = (s1_round, s2_round)
                
        return int(s2_round / n2)




        
# @lc code=end

