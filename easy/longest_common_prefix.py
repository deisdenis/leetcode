# problem origin: https://leetcode.com/problems/longest-common-prefix/
#
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#   Input: ["flower","flow","flight"]
#   Output: "fl"
#
# Example 2:
#   Input: ["dog","racecar","car"]
#   Output: ""
#   Explanation: There is no common prefix among the input strings.
#
# Note:
#   All given inputs are in lowercase letters a-z.


class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        # The solution is using horizontal scanning technique. Iterations are optimized by slicing longest possible
        # match pattern instead of incremental vertical search by numbers. Optimal solution depends on a context.
        #   time: O(n)
        #   space: O(1)
        if len(strs) > 0:
            match = strs[0]
            for i in range(1, len(strs)):
                while strs[i][:len(match)] != match:
                    match = match[:len(match)-1]
                if match == '':
                    break
            return match
        return ''


test_list = [["flower", "flow", "flight"], ["dog", "racecar", "car"], []]

answers = []

solution = Solution()
for test_value in test_list:
    answers.append(solution.longestCommonPrefix(test_value))
assert answers == ["fl", "", ""], str(answers) + ' is wrong solution'
print('Everything looks fine!')

