# origin: https://leetcode.com/problems/longest-palindromic-substring/
#
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#   Input: "babad"
#   Output: "bab"
#   Note: "aba" is also a valid answer.
#
#   Example 2:
#       Input: "cbbd"
#       Output: "bb"

class Solution:
    @staticmethod
    def is_palindrome(candidate):
        return candidate == candidate[::-1]

    def longestPalindrome(self, s: str) -> str:
        # time: O(n**2)
        # space: O(1)
        if len(s) == 0:
            return ''
        for max_len in range(len(s), 0, -1):
            for start_pos in range(0, len(s) - max_len + 1):
                if self.is_palindrome(s[start_pos:start_pos + max_len]):
                    return s[start_pos:start_pos + max_len]


test_list = ['babad', 'cbbd', '', 'z', 'zaq']
answers = []

solution = Solution()
for test_value in test_list:
    answers.append(solution.longestPalindrome(test_value))
assert answers == ['bab', 'bb', '', 'z', 'z'], str(answers) + ' is wrong solution'
print('Everything looks fine!')
