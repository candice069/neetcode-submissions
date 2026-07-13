# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #first, find the nth node
        #get the length of the list
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next
        
        dummy = ListNode(next=head)
        pre = dummy

        for _ in range(l-n):
            pre = pre.next

        pre.next = pre.next.next
        return dummy.next