#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#
# https://leetcode.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (59.70%)
# Likes:    539
# Dislikes: 798
# Total Accepted:    211.9K
# Total Submissions: 354.9K
# Testcase Example:  '1'
#
# Write a program that outputs the string representation of numbers from 1 to
# n.
# 
# But for multiples of three it should output “Fizz” instead of the number and
# for the multiples of five output “Buzz”. For numbers which are multiples of
# both three and five output “FizzBuzz”.
# 
# Example:
# 
# n = 15,
# 
# Return:
# [
# ⁠   "1",
# ⁠   "2",
# ⁠   "Fizz",
# ⁠   "4",
# ⁠   "Buzz",
# ⁠   "Fizz",
# ⁠   "7",
# ⁠   "8",
# ⁠   "Fizz",
# ⁠   "Buzz",
# ⁠   "11",
# ⁠   "Fizz",
# ⁠   "13",
# ⁠   "14",
# ⁠   "FizzBuzz"
# ]
# 
# 
#
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        """
        results = []
        for number in range(1, n+1):
            if number % 3 == 0 and number % 5 == 0:
                results.append("FizzBuzz")
            elif number % 5 == 0:
                results.append("Buzz")
            elif number % 3 == 0:
                results.append("Fizz")
            else:
                results.append(str(number))

        return results
        """

        ans = []
        fizz_buzz_dict = {3: "Fizz", 5: "Buzz"}

        for num in range(1, n+1):
            num_ans_str = ""
            for key in fizz_buzz_dict.keys():
                if num % key == 0:
                    num_ans_str += fizz_buzz_dict[key]

            if not num_ans_str:
                num_ans_str = str(num)

            ans.append(num_ans_str)

        return ans
        

