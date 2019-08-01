# origin: https://leetcode.com/problems/zigzag-conversion/
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);

# Example 1:
#   Input: s = "PAYPALISHIRING", numRows = 3
#   Output: "PAHNAPLSIIGYIR"
#
# Example 2:
#   Input: s = "PAYPALISHIRING", numRows = 4
#   Output: "PINALSIGYAHRPI"
#   Explanation:
#   P     I    N
#   A   L S  I G
#   Y A   H R
#   P     I

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # There are two ways to solve this. This one is passing characters one by one into the zigzag array. The
        # alternative is to add characters to the result by target indexes, however, both are O(n)
        # time O(n)
        # space O(n)
        if numRows == 1:
            return s
        data = [""]*numRows
        col = 0
        pos = 0
        while pos < len(s):
            if col % (numRows - 1) == 0:
                for r in range(numRows):
                    data[r] += s[pos]
                    pos += 1
                    if pos == len(s):
                        break
            else:
                data[numRows - 1 - col % (numRows - 1)] += s[pos]
                pos += 1
            col += 1

        answer = ""
        for row in data:
            answer += row
        return answer


test_list = [["PAYPALISHIRING", 3], ["PAYPALISHIRING", 4], ["A", 1]]
answers = []

solution = Solution()
for test_value in test_list:
    answers.append(solution.convert(test_value[0], test_value[1]))
assert answers == ["PAHNAPLSIIGYIR", "PINALSIGYAHRPI", "A"], str(answers) + ' is wrong solution'
print('Everything looks fine!')

