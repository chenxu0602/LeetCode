#
# @lc app=leetcode id=2836 lang=python3
#
# [2836] Maximize Value of Function in a Ball Passing Game
#

# @lc code=start
class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:

        
        # def apply(a, b):
        #     for to, score in a:
        #         new_id, add = b[to]
        #         yield new_id, score + add

        # power = [(to, v) for v, to in enumerate(receiver)]
        # bits = [*map(int, bin(k + 1)[:1:-1])]
        # powers = [power]

        # for _ in range(len(bits) - 1):
        #     power = list(apply(power, power))
        #     powers += power,

        # for p in (p for p, b in zip(powers[:-1], bits[:-1]) if b):
        #     power = list(apply(power, p))

        # return max(v for _, v in power)


        # Binary Jumping
        # Time  complexity: O(nlogk)
        # Space complexity: O(nlogk)

        n = len(receiver)
        parent, pathSum = [[0] * 35 for _ in range(n)], [[0] * 35 for _ in range(n)]
        for start in range(n):
            parent[start][0] = pathSum[start][0] = receiver[start]

        for power in range(1, 35):
            for start in range(n):
                parent[start][power] = parent[parent[start][power - 1]][power - 1]
                pathSum[start][power] = pathSum[start][power - 1] + pathSum[parent[start][power - 1]][power - 1]

        res = 0
        for start in range(n):
            i = start
            runningSum = 0
            for power in range(35):
                if k & (1 << power) != 0:
                    runningSum += pathSum[i][power]
                    i = parent[i][power]

            res = max(start + runningSum, res)

        return res
        
# @lc code=end

