# problem origin: https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#   Input: "abcabcbb"
#   Output: 3
#   Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
#   Input: "bbbbb"
#   Output: 1
#   Explanation: The answer is "b", with the length of 1.
#
# Example 3:
#   Input: "pwwkew"
#   Output: 3
#   Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # The solution could solve the proble in a single pass, but still could be optimized to a sliding window
        # to avoid additional checks of substrings that are already shorter than the longest one:
        #   time: O(n**2) -> iteration over all characters * iteration within substring
        #   space: O(n)
        # TODO: sliding window alghorithm
        maxl = 0
        subs = ''
        for let in s:
            if subs.find(let) == -1:
                subs += let
            else:
                subs = subs[subs.find(let)+1:] + let
            if maxl < len(subs):
                maxl = len(subs)
        return maxl


test_list = ['abcabcbb', 'bbbbb', 'pwwkew', 'dvdf']
answers = []

solution = Solution()
for test_value in test_list:
    answers.append(solution.lengthOfLongestSubstring(test_value))
assert answers == [3, 1, 3, 3], str(answers) + ' is wrong solution'
print('Everything looks fine!')