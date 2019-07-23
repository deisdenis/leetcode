class ListNode:
    def __init__(self, x):
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


def linked_list_from_list(lst):
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return ListNode(lst[0])
    else:
        prev = ListNode(0)
        first = prev
        for v in lst:
            prev.next = ListNode(v)
            prev = prev.next
        return first.next

