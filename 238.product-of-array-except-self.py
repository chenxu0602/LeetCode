#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # length = len(nums)
        # L, R, answer = [0]*length, [0]*length, [0]*length

        # L[0] = 1
        # for i in range(1, length):
        #     L[i] = nums[i-1] * L[i-1]

        # R[length-1] = 1
        # for i in range(length-2, -1, -1):
        #     R[i] = nums[i+1] * R[i+1]

        # for i in range(length):
        #     answer[i] = L[i] * R[i]

        # return answer

        n = len(nums)
        answers = [0] * n
        answers[0] = 1

        for i in range(1, n):
            answers[i] = nums[i-1] * answers[i-1]

        R = 1
        for i in range(n-1, -1, -1):
            answers[i] *= R
            R *= nums[i]

        return answers

        

