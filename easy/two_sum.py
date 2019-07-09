# problem origin: https://leetcode.com/problems/two-sum/
#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    # this approach can solve it within 1 pass leading to:
    #   time: O(n)
    #   space: O(n)
    def two_sum_single_pass(self, nums: list, target: int) -> list:
        d = {}
        for p in range(len(nums)):
            if (target - nums[p]) not in d:
                d[nums[p]] = p
            else:
                return [d[target-nums[p]], p]
    # this approach is inefficient in terms of time, but perfect in terms of space
    #   time: O(n**2)
    #   space: O(1)
    def two_sum_everything_for_space(self, nums: list, target: int) -> list:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


test_list = [2, 7, 11, 15]
test_target = 9

solution = Solution()
answer1 = solution.two_sum_single_pass(test_list, test_target)
assert answer1 == [0, 1], 'wrong solution'
answer2 = solution.two_sum_everything_for_space(test_list, test_target)
assert answer1 == [0, 1], 'wrong solution'
print('Everything looks fine!')
