#
# @lc app=leetcode id=1947 lang=python3
#
# [1947] Maximum Compatibility Score Sum
#

# @lc code=start
import itertools, heapq
from collections import defaultdict

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:

        # return max(sum(
        #     students[i][j] == mentors[perm[i]][j]
        #     for i in range(len(students))
        #     for j in range(len(students[0]))
        # ) for perm in itertools.permutations(range(len(students))))

        # m = len(students)
        # score = [[0] * m for _ in range(m)]

        # for i in range(m):
        #     for j in range(m):
        #         score[i][j] = sum(x == y for x, y in zip(students[i], mentors[j]))

        # ans = 0
        # for perm in itertools.permutations(range(m)):
        #     ans = max(ans, sum(score[i][j] for i, j in zip(perm, range(m))))
        # return ans

        m, n = map(len, (students, students[0]))
        def hamming(student, mentor):
            return sum([int(student[i] != mentor[i]) for i in range(n)])

        pq = [(0, 0, '0' * m)]
        optimal = defaultdict(lambda: float("inf"))

        while pq:
            cost, i, mentor_status = heapq.heappop(pq)

            if i == m: return m * n - cost

            for j, mentor in enumerate(mentors):
                if mentor_status[j] != '1':
                    new_cost = cost + hamming(students[i], mentor)
                    new_mentor_status = mentor_status[:j] + '1' + mentor_status[j + 1:]

                    if new_cost < optimal[(i + 1, new_mentor_status)]:
                        optimal[(i + 1, new_mentor_status)] = new_cost
                        heapq.heappush(pq, (new_cost, i + 1, new_mentor_status))

        return 0
        
# @lc code=end

