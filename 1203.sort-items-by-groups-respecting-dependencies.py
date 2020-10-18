#
# @lc app=leetcode id=1203 lang=python3
#
# [1203] Sort Items by Groups Respecting Dependencies
#
# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/description/
#
# algorithms
# Hard (45.94%)
# Likes:    119
# Dislikes: 27
# Total Accepted:    3.1K
# Total Submissions: 6.8K
# Testcase Example:  '8\n2\n[-1,-1,1,0,0,1,0,-1]\n[[],[6],[5],[6],[3,6],[],[],[]]'
#
# There are n items each belonging to zero or one of m groups where group[i] is
# the group that the i-th item belongs to and it's equal to -1 if the i-th item
# belongs to no group. The items and the groups are zero indexed. A group can
# have no item belonging to it.
# 
# Return a sorted list of the items such that:
# 
# 
# The items that belong to the same group are next to each other in the sorted
# list.
# There are some relations between these items where beforeItems[i] is a list
# containing all the items that should come before the i-th item in the sorted
# array (to the left of the i-th item).
# 
# 
# Return any solution if there is more than one solution and return an empty
# list if there is no solution.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems =
# [[],[6],[5],[6],[3,6],[],[],[]]
# Output: [6,3,4,1,5,2,0,7]
# 
# 
# Example 2:
# 
# 
# Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems =
# [[],[6],[5],[6],[3],[],[4],[]]
# Output: []
# Explanation: This is the same as example 1 except that 4 needs to be before 6
# in the sorted list.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= m <= n <= 3*10^4
# group.length == beforeItems.length == n
# -1 <= group[i] <= m-1
# 0 <= beforeItems[i].length <= n-1
# 0 <= beforeItems[i][j] <= n-1
# i != beforeItems[i][j]
# beforeItems[i] does not contain duplicates elements.
# 
# 
#

# @lc code=start
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topSort(al, i, res, stat):
            if stat[i] != 0:
                return stat[i] == 2
            stat[i] = 1
            for n in al[i]:
                if not topSort(al, n, res, stat):
                    return False

            stat[i] = 2
            res.append(i)
            return True

        res = []
        stat = [0] * (n + 2 * m)
        al = [set() for _ in range(n + 2 * m)]

        for i in range(n):
            if group[i] != -1:
                al[i].add(n + group[i])
                al[n + m + group[i]].add(i)

            for j in beforeItems[i]:
                if group[i] != -1 and group[i] == group[j]:
                    al[i].add(j)
                else:
                    if group[i] == -1:
                        ig, jg = group[i], group[j]
                    else:
                        ig, jg = n + group[i], n + m + group[j]

                    al[ig].add(jg)

        for n in range(len(al) - 1, -1, -1):
            if not topSort(al, n, res, stat):
                return []

        return res[:n]
        
# @lc code=end

