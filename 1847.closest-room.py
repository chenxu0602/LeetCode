#
# @lc app=leetcode id=1847 lang=python3
#
# [1847] Closest Room
#
# https://leetcode.com/problems/closest-room/description/
#
# algorithms
# Hard (26.94%)
# Likes:    149
# Dislikes: 7
# Total Accepted:    3.2K
# Total Submissions: 9.3K
# Testcase Example:  '[[2,2],[1,2],[3,2]]\n[[3,1],[3,3],[5,2]]'
#
# There is a hotel with n rooms. The rooms are represented by a 2D integer
# array rooms where rooms[i] = [roomIdi, sizei] denotes that there is a room
# with room number roomIdi and size equal to sizei. Each roomIdi is guaranteed
# to be unique.
# 
# You are also given k queries in a 2D array queries where queries[j] =
# [preferredj, minSizej]. The answer to the j^th query is the room number id of
# a room such that:
# 
# 
# The room has a size of at least minSizej, and
# abs(id - preferredj) is minimized, where abs(x) is the absolute value of x.
# 
# 
# If there is a tie in the absolute difference, then use the room with the
# smallest such id. If there is no such room, the answer is -1.
# 
# Return an array answer of length k where answer[j] contains the answer to the
# j^th query.
# 
# 
# Example 1:
# 
# 
# Input: rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]
# Output: [3,-1,3]
# Explanation: The answers to the queries are as follows:
# Query = [3,1]: Room number 3 is the closest as abs(3 - 3) = 0, and its size
# of 2 is at least 1. The answer is 3.
# Query = [3,3]: There are no rooms with a size of at least 3, so the answer is
# -1.
# Query = [5,2]: Room number 3 is the closest as abs(3 - 5) = 2, and its size
# of 2 is at least 2. The answer is 3.
# 
# Example 2:
# 
# 
# Input: rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]
# Output: [2,1,3]
# Explanation: The answers to the queries are as follows:
# Query = [2,3]: Room number 2 is the closest as abs(2 - 2) = 0, and its size
# of 3 is at least 3. The answer is 2.
# Query = [2,4]: Room numbers 1 and 3 both have sizes of at least 4. The answer
# is 1 since it is smaller.
# Query = [2,5]: Room number 3 is the only room with a size of at least 5. The
# answer is 3.
# 
# 
# Constraints:
# 
# 
# n == rooms.length
# 1 <= n <= 10^5
# k == queries.length
# 1 <= k <= 10^4
# 1 <= roomIdi, preferredj <= 10^7
# 1 <= sizei, minSizej <= 10^7
# 
# 
# 
#

# @lc code=start
import bisect

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:

        rooms.sort(key=lambda x: x[1], reverse=True)
        qArr = [[i, q] for i, q in enumerate(queries)]
        qArr.sort(key=lambda x: x[1][1], reverse=True)

        def searchClosestRoomId(preferredId):
            if len(roomIdsSoFar) == 0: return -1
            cands = []
            i = bisect.bisect_right(roomIdsSoFar, preferredId)
            if i > 0:
                cands.append(roomIdsSoFar[i - 1])
            if i < len(roomIdsSoFar):
                cands.append(roomIdsSoFar[i])
            return min(cands, key=lambda x: abs(x - preferredId))

        roomIdsSoFar = []
        n, k = len(rooms), len(queries)
        i = 0
        ans = [-1] * k

        for index, (preferredId, minSize) in qArr:
            while i < n and rooms[i][1] >= minSize:
                bisect.insort(roomIdsSoFar, rooms[i][0])
                i += 1
            ans[index] = searchClosestRoomId(preferredId)

        return ans


        
# @lc code=end

