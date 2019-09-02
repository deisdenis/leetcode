# origin: https://leetcode.com/problems/implement-strstr/
#
# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#   Input: haystack = "hello", needle = "ll"
#   Output: 2

# Example 2:
#   Input: haystack = "aaaaa", needle = "bba"
#   Output: -1

# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		if len(needle) == 0:
			return 0
		for p in range(len(haystack) - len(needle) + 1):
			slider = 0
			while haystack[p + slider] == needle[slider]:
				slider += 1
				if slider == len(needle):
					return p
		return -1


test_list = [["hello", "ll"], ["aaaaa", "bba"], ["cats", ""], ["", "qwe"]]

answers = []

solution = Solution()
for test_value in test_list:
	answers.append(solution.strStr(test_value[0], test_value[1]))
assert answers == [2, -1, 0, -1], str(answers) + ' is wrong solution'
print('Everything looks fine!')
