#
# @lc app=leetcode id=1086 lang=python3
#
# [1086] High Five
#
# https://leetcode.com/problems/high-five/description/
#
# algorithms
# Easy (74.67%)
# Likes:    65
# Dislikes: 19
# Total Accepted:    8.7K
# Total Submissions: 11.6K
# Testcase Example:  '[[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]'
#
# Given a list of scores of different students, return the average score of
# each student's top five scores in the order of each student's id.
# 
# Each entry items[i] has items[i][0] the student's id, and items[i][1] the
# student's score.  The average score is calculated using integer division.
# 
# 
# 
# Example 1:
# 
# 
# Input:
# [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# Output: [[1,87],[2,88]]
# Explanation: 
# The average of the student with id = 1 is 87.
# The average of the student with id = 2 is 88.6. But with integer division
# their average converts to 88.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= items.length <= 1000
# items[i].length == 2
# The IDs of the students is between 1 to 1000
# The score of the students is between 1 to 100
# For each student, there are at least 5 scores
# 
#
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(reverse=True)
        m, s = 0, []
        while m < len(items):
            if m == 0 or items[m-1][0] != items[m][0]:
                n = 0
                for _, v in items[m:m+5]:
                    n += v
                s.append([items[m][0], n//5])
                m += 5
            else:
                m += 1
        return s[::-1]

        

