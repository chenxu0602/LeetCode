#
# @lc app=leetcode id=2201 lang=python3
#
# [2201] Count Artifacts That Can Be Extracted
#

# @lc code=start
class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:

        dig = set((r, c) for r, c in dig)

        count = 0
        for r1, c1, r2, c2 in artifacts:
            positions = set()
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    positions.add((r, c))

            if all([pos in dig for pos in positions]):
                count += 1

        return count
        
# @lc code=end

