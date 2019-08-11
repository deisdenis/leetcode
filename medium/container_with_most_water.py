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
        # The idea is to use sliding borders, as only the lower boundary is responsible for the height.
        # time: O(n)
        # space: O(1)
        left = 0
        right = len(height) - 1
        max_area = min(height[left], height[right]) * right
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            if min(height[left], height[right])*(right - left) > max_area:
                max_area = min(height[left], height[right])*(right - left)
        return max_area


test_list = [[1, 8, 6, 2, 5, 4, 8, 3, 7], [3, 5], np.arange(15000, 0, -1)]
answers = []

solution = Solution()
for test_value in test_list:
    answers.append(solution.maxArea(test_value))
assert answers == [49, 3, 56250000], str(answers) + ' is wrong solution'
print('Everything looks fine!')
