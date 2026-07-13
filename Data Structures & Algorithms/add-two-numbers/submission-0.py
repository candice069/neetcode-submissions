# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #two pointers
        p1 = l1
        p2 = l2

        #create an empty node to start the result linkedList
        dummy = ListNode()
        cur = dummy

        left = 0
        while p1 or p2 or left:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            digit = (v1 + v2 + left) % 10
            left = (v1 + v2 + left) // 10

            new_node = ListNode(val = digit)
            cur.next = new_node
            cur= new_node

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        return dummy.next
