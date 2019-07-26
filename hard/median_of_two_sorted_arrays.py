# problem origin: https://leetcode.com/problems/median-of-two-sorted-arrays/
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#   nums1 = [1, 3]
#   nums2 = [2]
#   The median is 2.0
#
# Example 2:
#   nums1 = [1, 2]
#   nums2 = [3, 4]
#   The median is (2 + 3)/2 = 2.5

class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        # The solution is not optimal and could be improved up to time complexity O(log(min(m, n))
        #   time: O((m+n)/2)
        #   space: O(1)
        # TODO: optimize by time
        is_odd = (len(nums1) + len(nums2)) % 2
        target = (len(nums1) + len(nums2)) // 2 + is_odd
        pos = 1
        i = 0
        j = 0
        while pos < target and i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
            pos += 1

        # TODO: could be optimized by removing iteration
        while pos != target and i < len(nums1):
            i += 1
            pos += 1

        while pos != target and j < len(nums2):
            j += 1
            pos += 1

        if i == len(nums1):
            answer = nums2[j]
            if is_odd == 0:
                answer = (answer + nums2[j+1])/2.0
            return answer

        if j == len(nums2):
            answer = nums1[i]
            if is_odd == 0:
                answer = (answer + nums1[i+1])/2.0
            return answer

        if nums1[i] < nums2[j]:
            answer = nums1[i]
            i += 1
        else:
            answer = nums2[j]
            j += 1

        if is_odd == 0:
            if i == len(nums1):
                answer = (answer + nums2[j])/2.0

            elif j == len(nums2):
                answer = (answer + nums1[i])/2.0

            elif nums1[i] < nums2[j]:
                answer = (answer + nums1[i])/2.0
            else:
                answer = (answer + nums2[j])/2.0

        return answer



test_list = [[[1, 3], [2]], [[1, 2], [3, 4]], [[], [1, 2, 3, 4, 5]]]
answers = []

solution = Solution()
for test_value in test_list:
    answers.append(solution.findMedianSortedArrays(test_value[0], test_value[1]))
assert answers == [2.0, 2.5, 3.0], str(answers) + ' is wrong solution'
print('Everything looks fine!')
