# origin: https://leetcode.com/problems/container-with-most-water/
#
# Given n non - negative integers a1, a2, ..., an, where each represents a point at coordinate(i, ai).n vertical lines
# are drawn such that the two endpoints of line i is at(i, ai) and (i, 0).Find two lines, which together with x - axis
# forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at
# least 2.  The above vertical lines are represented by array[1, 8, 6, 2, 5, 4, 8, 3, 7].In this case, the max area of
# water(blue section) the container can contain is 49.
#
# Example:
#     Input: [1, 8, 6, 2, 5, 4, 8, 3, 7]
#     Output: 49
import numpy as np


class Solution:
    def maxArea(self, height: list) -> int:
        height = np.array(height)
        n = len(height)
        # get distances
        d = np.matmul(np.arange(n).reshape(n, 1), np.ones((1, n)))
        dist = abs(d - d.T)
        # get heights
        h1m = np.matmul(height.reshape(n, 1), np.ones((1, n)))
        h2m = np.matmul(np.ones((n, 1)), height.reshape(n, 1).T)
        h1g = np.less_equal(h1m, h2m)
        h2g = np.less(h2m, h1m)
        ans = h1g * h1m + h2g * h2m
        areas = ans * dist
        return areas.max()


test_list = [[1, 8, 6, 2, 5, 4, 8, 3, 7], [3, 5]]
answers = []

solution = Solution()
for test_value in test_list:
    answers.append(solution.maxArea(test_value))
assert answers == [49, 3], str(answers) + ' is wrong solution'
print('Everything looks fine!')
