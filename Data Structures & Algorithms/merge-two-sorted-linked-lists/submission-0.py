# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy

        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val < p2.val:
                prev.next = p1
                prev = p1
                p1 = p1.next
            else:
                prev.next = p2
                prev = p2
                p2 = p2.next
        if p1:
            prev.next = p1
        if p2:
            prev.next = p2
        return dummy.next