#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#
# https://leetcode.com/problems/queue-reconstruction-by-height/description/
#
# algorithms
# Medium (59.91%)
# Likes:    1623
# Dislikes: 182
# Total Accepted:    81.7K
# Total Submissions: 136K
# Testcase Example:  '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]'
#
# Suppose you have a random list of people standing in a queue. Each person is
# described by a pair of integers (h, k), where h is the height of the person
# and k is the number of people in front of this person who have a height
# greater than or equal to h. Write an algorithm to reconstruct the queue.
# 
# 
# Note:
# The number of people is less than 1,100.
# 
# 
# 
# 
# Example
# 
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# 
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
# 
# 
#
from collections import defaultdict

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        if not people: return []

        peopledict, heights, res = defaultdict(list), [], []

        for i in range(len(people)):
            p = people[i]
            if not p[0] in peopledict:
                heights.append(p[0])
            peopledict[p[0]].append((p[1], i))

        heights.sort()

        print(peopledict)

        for h in heights[::-1]:
            peopledict[h].sort()
            for p in peopledict[h]:
                print(f"h={h}, p0={p[0]}, p1={p[1]}")
                res.insert(p[0], people[p[1]])

        print(res)
        return res
        """

        people.sort(key=lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output
        

