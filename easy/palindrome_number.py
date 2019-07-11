# problem origin: https://leetcode.com/problems/reverse-integer/
#
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Example 1:
#   Input: 121
#   Output: true
#
# Example 2:
#   Input: -121
#   Output: false
#   Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#
# Example 3:
#   Input: 10
#   Output: false
#   Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution:
    # The solution with string conversion is out of the scope. To work with numbers we will revert first half of the
    # number and compare the remaining part with it.
    #   time: O(log(n))
    #   space: O(1)
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): # negative numbers and 0 endings are not palindromes
            return False
        y = 0
        while x > y:
            y = y * 10 + x % 10
            x //= 10
        return x == y or x == y // 10 # second check is for odd len numbers


test_list = [123, -123, 12321, 10]

answers = []

solution = Solution()
for test_value in test_list:
    answers.append(solution.isPalindrome(test_value))
assert answers == [False, False, True, False], str(answers) + ' is wrong solution'
print('Everything looks fine!')
