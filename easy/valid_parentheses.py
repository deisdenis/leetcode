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
        # The solution uses single pass based on dictionary and stack of open parentheses to keep reverse closing order:
        #   time: O(n)
        #   space: O(n)
        brackets = {')': '(', ']': '[', '}': '{'}
        debt = []
        for char in s:
            if char in brackets:
                if len(debt) == 0 or debt.pop() != brackets[char]:
                    return False
            else:
                debt.append(char)
        if len(debt) > 0:
            return False
        return True


test_list = ["()", "()[]{}", "(]", "([)]", "{[]}", "]", "[", "[([]])", "(])"]
answers = []

solution = Solution()
for test_value in test_list:
    answers.append(solution.isValid(test_value))
assert answers == [True, True, False, False, True, False, False, False, False], str(answers) + ' is wrong solution'
print('Everything looks fine!')

