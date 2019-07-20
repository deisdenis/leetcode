# problem origin: https://leetcode.com/problems/valid-parentheses/
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#   Open brackets must be closed by the same type of brackets.
#   Open brackets must be closed in the correct order.
#   Note that an empty string is also considered valid.
#
# Example 1:
#   Input: "()"
#   Output: true
#
# Example 2:
#   Input: "()[]{}"
#   Output: true
#
# Example 3:
#   Input: "(]"
#   Output: false
#
# Example 4:
#   Input: "([)]"
#   Output: false
#
# Example 5:
#   Input: "{[]}"
#   Output: true


class Solution:
    def isValid(self, s: str) -> bool:
        #dict = {'(': 0, ')': 0, '[': 0, ']': 0, '{': 0, '}': 0}
        dict = {'()': 0, '[]': 0, '{}': 0}
        for char in s:
            dict[char] += 1
            if ((dict['}'] > dict['{']) or (dict[']'] > dict['[']) or (dict[')'] > dict['('])) \
                    or ((dict['}'] < dict['{']) and ((dict[']'] != dict['[']) or (dict[')'] != dict['(']))) \
                    or ((dict[']'] < dict['[']) and ((dict[')'] != dict['(']) or (dict['}'] != dict['{']))) \
                    or (((dict['}'] != dict['{']) or (dict[']'] != dict['['])) and (dict[')'] < dict['('])):
                return False

        return True


test_list = ["()", "()[]{}", "(]", "([)]", "{[]}"]

answers = []

solution = Solution()
for test_value in test_list:
    answers.append(solution.isValid(test_value))
assert answers == [True, True, False, False, True], str(answers) + ' is wrong solution'
print('Everything looks fine!')

