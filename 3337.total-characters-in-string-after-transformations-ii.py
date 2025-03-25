#
# @lc app=leetcode id=3337 lang=python3
#
# [3337] Total Characters in String After Transformations II
#

# @lc code=start
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:

        def mat_mul(mat1, mat2, MOD):
            mat = [[0] * len(mat2[0]) for _ in range(len(mat1))]
            for i in range(len(mat1)):
                for j in range(len(mat2[0])):
                    for k in range(len(mat2)):
                        mat[i][j] += mat1[i][k] * mat2[k][j]
                    mat[i][j] %= MOD
            return mat

        def mat_pow(mat, n, MOD):
            size = len(mat)
            res = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
            while n > 0:
                if n & 1:
                    res = mat_mul(res, mat, MOD)
                mat = mat_mul(mat, mat, MOD)
                n >>= 1
            return res


        MOD = 10 ** 9 + 7
        matrix = [[0] * 26 for _ in range(26)]
        for i, k in enumerate(nums):
            for j in range(i + 1, i + k + 1):
                matrix[i][j % 26] = 1

        matrix_t = mat_pow(matrix, t, MOD)
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        res = mat_mul([count], matrix_t, MOD)
        return sum(res[0]) % MOD

        
        
# @lc code=end

