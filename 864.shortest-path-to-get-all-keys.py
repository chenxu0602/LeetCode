#
# @lc app=leetcode id=864 lang=python3
#
# [864] Shortest Path to Get All Keys
#
# https://leetcode.com/problems/shortest-path-to-get-all-keys/description/
#
# algorithms
# Hard (40.09%)
# Likes:    403
# Dislikes: 13
# Total Accepted:    10.5K
# Total Submissions: 25.8K
# Testcase Example:  '["@.a.#","###.#","b.A.B"]'
#
# We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@"
# is the starting point, ("a", "b", ...) are keys, and ("A", "B", ...) are
# locks.
# 
# We start at the starting point, and one move consists of walking one space in
# one of the 4 cardinal directions.  We cannot walk outside the grid, or walk
# into a wall.  If we walk over a key, we pick it up.  We can't walk over a
# lock unless we have the corresponding key.
# 
# For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter
# of the first K letters of the English alphabet in the grid.  This means that
# there is exactly one key for each lock, and one lock for each key; and also
# that the letters used to represent the keys and locks were chosen in the same
# order as the English alphabet.
# 
# Return the lowest number of moves to acquire all keys.  If it's impossible,
# return -1.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["@.a.#","###.#","b.A.B"]
# Output: 8
# 
# 
# 
# Example 2:
# 
# 
# Input: ["@..aA","..B#.","....b"]
# Output: 6
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length <= 30
# 1 <= grid[0].length <= 30
# grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F'
# The number of keys is in [1, 6].  Each key has a different letter and opens
# exactly one lock.
# 
# 
# 
#

# @lc code=start
from collections import defaultdict, deque
import heapq, itertools

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        # Brute Force + Permutations
        # Time  complexity: O(R x C x A x A!), where R, C are the dimensions of the grid,
        # and A is the maximum number of keys.
        # Space compleixty: O(R x C + A!)
        # R, C = map(len, (grid, grid[0]))
        # location = {v: (r, c)
        #             for r, row in enumerate(grid)
        #             for c, v in enumerate(row)
        #             if v not in '.#'}

        # def neighbors(r, c):
        #     for cr, cc in (r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1):
        #         if 0 <= cr < R and 0 <= cc < C:
        #             yield cr, cc

        # def bfs(source, target, keys=()):
        #     sr, sc = location[source]
        #     tr, tc = location[target]
        #     seen = [[False] * C for _ in range(R)]
        #     seen[sr][sc] = True
        #     queue = deque([(sr, sc, 0)])
        #     while queue:
        #         r, c, d = queue.popleft()
        #         if r == tr and c == tc: return d
        #         for cr, cc in neighbors(r, c):
        #             if not seen[cr][cc] and grid[cr][cc] != '#':
        #                 if grid[cr][cc].isupper() and grid[cr][cc].lower() not in keys:
        #                     continue
        #                 queue.append((cr, cc, d + 1))
        #                 seen[cr][cc] = True
        #     return float("inf")

        # ans = float("inf")
        # keys = "".join(chr(ord('a') + i) for i in range(len(location) // 2))
        # for cand in itertools.permutations(keys):
        #     bns = 0
        #     for i, target in enumerate(cand):
        #         source = cand[i - 1] if i > 0 else '@'
        #         d = bfs(source, target, cand[:i])
        #         bns += d
        #         if bns >= ans: break
        #     else:
        #         ans = bns

        # return ans if ans < float("inf") else -1



        # Points of Interest + Dijkstra
        # Time  complexity: O(RC(2A + 1) + ElogN), where R, C are the dimensions of the grid, 
        # and A is the maximum number of keys, N = (2A + 1) x 2^A is the number of nodes when we
        # perform Dijkstra's, and E = N x (2A + 1) is the maximum number of edges.
        # Space complexity: ON(N)
        R, C = len(grid), len(grid[0])

        # The points of interest
        location = {v: (r, c)
                    for r, row in enumerate(grid)
                    for c, v in enumerate(row)
                    if v not in '.#'}

        def neighbors(r, c):
            for cr, cc in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if 0 <= cr < R and 0 <= cc < C:
                    yield cr, cc

        # The distance from source to each point of interest
        def bfs_from(source):
            r, c = location[source]
            seen = [[False] * C for _ in range(R)]
            seen[r][c] = True
            queue = deque([(r, c, 0)])
            dist = {}
            while queue:
                r, c, d = queue.popleft()
                if source != grid[r][c] != '.':
                    dist[grid[r][c]] = d
                    continue # Stop walking from here if we reach a point of interest
                for cr, cc in neighbors(r, c):
                    if grid[cr][cc] != '#' and not seen[cr][cc]:
                        seen[cr][cc] = True
                        queue.append((cr, cc, d + 1))
            return dist        

        dists = {place: bfs_from(place) for place in location}
        target_state = 2 ** sum(p.islower() for p in location) - 1

        #Dijkstra
        pq = [(0, '@', 0)]
        final_dist = defaultdict(lambda: float('inf'))
        final_dist['@', 0] = 0
        while pq:
            d, place, state = heapq.heappop(pq)
            if final_dist[place, state] < d: continue
            if state == target_state: return d
            for destination, d2 in dists[place].items():
                state2 = state
                if destination.islower(): #key
                    state2 |= 1 << ord(destination) - ord('a')
                elif destination.isupper(): #lock
                    if not(state & (1 << ord(destination) - ord('A'))): #no key
                        continue

                if d + d2 < final_dist[destination, state2]:
                    final_dist[destination, state2] = d + d2
                    heapq.heappush(pq, (d + d2, destination, state2))

        return -1

# @lc code=end

