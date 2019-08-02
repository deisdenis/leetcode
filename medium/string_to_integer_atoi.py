# origin: https://leetcode.com/problems/string-to-integer-atoi/
#
# Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is
# found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical
# digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number, which are ignored and have no
# effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence
# exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
#   Only the space character ' ' is considered as whitespace character.
#   Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
#   [−2**31,  2**31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (2**31 − 1) or
#   INT_MIN (−2**31) is returned.
#
# Example 1:
#   Input: "42"
#   Output: 42
#
# Example 2:
#   Input: "   -42"
#   Output: -42
#   Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.
#
# Example 3:
#   Input: "4193 with words"
#   Output: 4193
#   Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
#
# Example 4:
#   Input: "words and 987"
#   Output: 0
#   Explanation: The first non-whitespace character is 'w', which is not a numerical
#              digit or a +/- sign. Therefore no valid conversion could be performed.

# Example 5:
#   Input: "-91283472332"
#   Output: -2147483648
#   Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−231) is returned.


class Solution:
    def myAtoi(self, str: str) -> int:
        # time: O(n) - n->len(str)
        # space: O(1)
        result = 0
        started = False
        sign = 1
        numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7':7, '8':8, '9':9}
        for char in str:
            if not started:
                if char == ' ':
                    pass
                elif char == '-':
                    started = True
                    sign = -1
                elif char == '+':
                    started = True
                elif char in numbers:
                    started = True
                    result = numbers[char]
                else:
                    return 0
            elif started:
                if char in numbers:
                    if result > 2**31//10:
                        if sign == 1:
                            return 2**31-1
                        else:
                            return -2**31
                    elif result == 2**31//10:
                        if sign == 1:
                            if numbers[char] <= 7:
                                return result * 10 + numbers[char]
                            else:
                                return 2 ** 31 - 1
                        else:
                            if numbers[char] <= 8:
                                return -1*(result * 10 + numbers[char])
                            else:
                                return -2 ** 31
                    else:
                        result = result * 10 + numbers[char]
                else:
                    break
        return sign * result


test_list = ["42", "   -42", "4193 with words", "words and 987", "-91283472332", "+1"]
answers = []

solution = Solution()
for test_value in test_list:
    answers.append(solution.myAtoi(test_value))
assert answers == [42, -42, 4193, 0, -2147483648, 1], str(answers) + ' is wrong solution'
print('Everything looks fine!')

