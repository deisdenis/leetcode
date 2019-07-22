# problem origin: https://leetcode.com/problems/merge-two-sorted-lists/
#
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#   Input: 1->2->4, 1->3->4
#   Output: 1->1->2->3->4->4


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


    def __str__(self):
        nxt = self
        s = str(nxt.val)
        while nxt.next is not None:
            s += '->'
            nxt = nxt.next
            s += str(nxt.val)
        return s


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # The solution is comparing both lists in parallel and stacking the result into the third linked list.
        #   time: O(n) -> n is sum of nodes in both lists
        #   space: O(n)
        l3 = ListNode(0)
        prev = l3
        while (l1 is not None) and (l2 is not None):
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        if l1 is None:
            prev.next = l2
        if l2 is None:
            prev.next = l1
        return l3.next


ln11 = ListNode(1)
ln12 = ListNode(2)
ln13 = ListNode(4)
ln11.next = ln12
ln12.next = ln13

ln21 = ListNode(1)
ln22 = ListNode(3)
ln23 = ListNode(4)
ln21.next = ln22
ln22.next = ln23

test_list = [[ln11, ln21]]

answers = []

solution = Solution()
for test_value in test_list:
    answers.append(str(solution.mergeTwoLists(test_value[0], test_value[1])))
assert answers == ["1->1->2->3->4->4"], str(answers) + ' is wrong solution'
print('Everything looks fine!')

#TODO refactor test function as a separate module

