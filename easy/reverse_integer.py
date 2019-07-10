# problem origin: https://leetcode.com/problems/reverse-integer/
#
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#   Input: 123
#   Output: 321
#
# Example 2:
#   Input: -123
#   Output: -321
#
# Example 3:
#   Input: 120
#   Output: 21
#
# Note:
#   Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
#   [−2**31,  2**31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer
#   overflows.


class Solution:
    # The idea is to pop and push digits one by one into target variable. There are 3 tricky points:
    #   1) Floor division of a negative number could be confusing (e.g. -12 // 10 = -3), to avoid this will use int,
    #       it will provide digit towards 0.
    #   2) Modulo operation of negative numbers is also confusing (e.g. -12 % 10 = 8), this happens because python
    #       always yields integer of the same sign as the divisor. To avoid this we will use negative divisor
    #       for negative numbers.
    #   3) We need to check variable before assignment due to environment limitation, direct comparison like
    #       -2**31 <= answer <= 2**31-1 is cheating
    #   time: O(log(n))
    #   space: O(n)
    def reverse(self, x: int) -> int:

        answer = 0
        MAX_INT_LIMIT = int((2**31-1) / 10)
        MIN_INT_LIMIT = int(-2**31 / 10)
        while x != 0:
            if x >= 0:
                if (answer < MAX_INT_LIMIT) or ((answer == MAX_INT_LIMIT) and (x % 10 <= 7)):
                    answer = answer * 10 + x % 10
                    x = int(x / 10)
                else:
                    return 0
            else:
                if (answer > MIN_INT_LIMIT) or (answer == MIN_INT_LIMIT and x % -10 <= 8):
                    answer = answer * 10 + x % -10
                    x = int(x / 10)
                else:
                    return 0

        return answer


test_list = [123, -123, 120, 7463847412, 2147483648, -2147483648, -2147483647, -10, 901000, -1463847412]
answers = []

solution = Solution()
for test_value in test_list:
    answers.append(solution.reverse(test_value))
assert answers == [321, -321, 21, 2147483647, 0, 0, 0, -1, 109, -2147483641], str(answers) + ' is wrong solution'
print('Everything looks fine!')
