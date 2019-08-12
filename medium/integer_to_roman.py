# origin: https://leetcode.com/problems/integer-to-roman/
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
#
# Example 1:
#   Input: 3
#   Output: "III"
#
# Example 2:
#   Input: 4
#   Output: "IV"
#
# Example 3:
#   Input: 9
#   Output: "IX"
#
# Example 4:
#   Input: 58
#   Output: "LVIII"
#   Explanation: L = 50, V = 5, III = 3.
#
# Example 5:
#   Input: 1994
#   Output: "MCMXCIV"
#   Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


class Solution:
    def intToRoman(self, num: int) -> str:
        # The idea is to use dictionary and "translate an integer to roman step by step.
        # time: O(n) -> n is length of an int (limited to 4 by the input)
        # space: O(1)
        converter = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        answer = ''
        mult = 1
        while num > 0:
            val = num % 10
            if val == 9:
                answer = converter[mult] + converter[mult*10] + answer
            elif val >= 5:
                answer = converter[mult*5] + converter[mult] * (val - 5) + answer
            elif val == 4:
                answer = converter[mult] + converter[mult*5] + answer
            elif val > 0:
                answer = converter[mult] * val + answer
            num = num // 10
            mult *= 10
        return answer


test_list = [3, 4, 9, 58, 1994, 3999]
answers = []

solution = Solution()
for test_value in test_list:
    answers.append(solution.intToRoman(test_value))
assert answers == ["III", "IV", "IX", "LVIII", "MCMXCIV", "MMMCMXCIX"], str(answers) + ' is wrong solution'
print('Everything looks fine!')
