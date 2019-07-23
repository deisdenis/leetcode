# problem origin: https://leetcode.com/problems/add-two-numbers/
#
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#   Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#   Output: 7 -> 0 -> 8
#   Explanation: 342 + 465 = 807.

# Definition for singly-linked list.

from common.common import ListNode, linked_list_from_list

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # The solution is straightforward and based on a single parallel pass of both lists:
        #   time: O(n) -> n is the length of the longest linked list
        #   space: O(n)
        answer = ListNode(0)
        prev = answer
        buffer = 0
        while l1 is not None and l2 is not None:
            val = l1.val + l2.val + buffer
            buffer = val // 10
            prev.next = ListNode(val % 10)
            prev = prev.next
            l1 = l1.next
            l2 = l2.next
        if l1 is not None:
            while buffer != 0 and l1 is not None:
                val = l1.val + buffer
                buffer = val // 10
                prev.next = ListNode(val % 10)
                prev = prev.next
                l1 = l1.next
            if l1 is not None:
                prev.next = l1
        if l2 is not None:
            while buffer != 0 and l2 is not None:
                val = l2.val + buffer
                buffer = val // 10
                prev.next = ListNode(val % 10)
                prev = prev.next
                l2 = l2.next
            if l2 is not None:
                prev.next = l2
        if buffer == 1:
            prev.next = ListNode(1)
        return answer.next


ln1 = linked_list_from_list([2, 4, 3])
ln2 = linked_list_from_list([5, 6, 4])

test_list = [[linked_list_from_list([2, 4, 3]), linked_list_from_list([5, 6, 4])], [linked_list_from_list([5]), linked_list_from_list([5])],
             [linked_list_from_list([1]), linked_list_from_list([9, 9])], [linked_list_from_list([1, 8]), linked_list_from_list([0])],
             [linked_list_from_list([0]), linked_list_from_list([7, 3])]]

answers = []

solution = Solution()
for test_value in test_list:
    answers.append(str(solution.addTwoNumbers(test_value[0], test_value[1])))
assert answers == ["7->0->8", "0->1", "0->0->1", "1->8", "7->3"], str(answers) + ' is wrong solution'
print('Everything looks fine!')
