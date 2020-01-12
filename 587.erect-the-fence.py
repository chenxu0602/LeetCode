#
# @lc app=leetcode id=587 lang=python3
#
# [587] Erect the Fence
#
# https://leetcode.com/problems/erect-the-fence/description/
#
# algorithms
# Hard (34.45%)
# Likes:    141
# Dislikes: 151
# Total Accepted:    7.2K
# Total Submissions: 20.8K
# Testcase Example:  '[[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]'
#
# There are some trees, where each tree is represented by (x,y) coordinate in a
# two-dimensional garden. Your job is to fence the entire garden using the
# minimum length of rope as it is expensive. The garden is well fenced only if
# all the trees are enclosed. Your task is to help find the coordinates of
# trees which are exactly located on the fence perimeter.
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
# Explanation:
# 
# 
# 
# Example 2:
# 
# 
# Input: [[1,2],[2,2],[4,2]]
# Output: [[1,2],[2,2],[4,2]]
# Explanation:
# 
# Even you only have trees in a line, you need to use rope to enclose
# them. 
# 
# 
# 
# 
# Note:
# 
# 
# All trees should be enclosed together. You cannot cut the rope to enclose
# trees that will separate them in more than one group.
# All input integers will range from 0 to 100.
# The garden has at least one tree.
# All coordinates are distinct.
# Input points have NO order. No order required for output.
# input types have been changed on April 15, 2019. Please reset to default code
# definition to get new method signature.
# 
# 
#
class Solution:
    def orientation(self, p, q, r):
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    def inBetween(self, p, i, q):
        a = i[0] >= p[0] and i[0] <= q[0] or i[0] <= p[0] and i[0] >= q[0]
        b = i[1] >= p[1] and i[1] <= q[1] or i[1] <= p[1] and i[1] >= q[1]
        return a and b

    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        hull = []
        if len(points) < 4:
            for p in points:
                hull.append(p)
            return hull

        left_most = 0
        for i in range(len(points)):
            if points[i][0] < points[left_most][0]:
                left_most = i

        p = left_most
        while True:
            q = (p + 1) % len(points)
            for i in range(len(points)):
                if self.orientation(points[p], points[i], points[q]) < 0:
                    q = i

            for i in range(len(points)):
                if i != p and i != q and self.orientation(points[p], points[i], points[q]) == 0 \
                    and self.inBetween(points[p], points[i], points[q]):
                    hull.append(points[i])

            hull.append(points[q])
            p = q
            if p == left_most:
                break

        return hull
            
        

